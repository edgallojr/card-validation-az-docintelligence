import streamlit as st
from services.blob_services import upload_blob
from services.credit_card_services import analyze_credit_card




def configure_interface():
    st.title("Upload de Arquivo - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo para upload", type=["pdf", "png", "jpg", "jpeg"])

    if uploaded_file is not None:   
        fileName = uploaded_file.name
        # enviar o arquivo para o Azure Blob Storage #  
        blob_url = upload_blob(uploaded_file, fileName)
    
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso!")
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Falha ao enviar o arquivo {fileName}.")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Arquivo enviado",width="stretch")
    st.write("Resultado da validaçao:")
    if credit_card_info and credit_card_info ["card_name"] and credit_card_info ["card_number"] and credit_card_info ["expiry_date"]:
        st.markdown(f"<h1 style='color: green;'>Válido</h1>", unsafe_allow_html=True) 
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
        st.write(f"Número do Cartão: {credit_card_info['card_number']}")   
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido.")

if __name__ == "__main__":
    configure_interface()
       