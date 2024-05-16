import streamlit as st
from streamlit_custom_notification_box import custom_notification_box

class Classifier():
    def __init__(self):
        pass

    def run(self):
        st.title('Classificador de Demônios de Persona e Shin Megami Tensei')

        st.write('Este é um classificador de demônios de Persona e Shin Megami Tensei. Ele foi treinado para identificar Pixie, Jack Frost e Decarabia')
        st.write('Para usá-lo, basta fazer o upload de uma imagem de um desses demônios e clicar em "Classificar". Para melhores resultados, use imagens recortadas.')
        st.write('Escolha quantas imagens deseja classificar.')
        with st.form("my-form", clear_on_submit=True):
            image = st.file_uploader(f'Faça o upload da imagem', type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
            col1, col2 = st.columns(2, gap="large")
            with col1:
                classify_button = st.form_submit_button('Classificar')
            with col2:    
                clear_button = st.form_submit_button('Limpar')

            if classify_button:
                if image != []:
                    st.write('Classificando...')
                    for i in range(len(image)):
                        st.image(image[i], width=150)
                else:
                    st.write('Por favor, faça o upload de uma imagem antes de clicar em "Classificar"')

            if clear_button:
                pass

if __name__ == '__main__':
    Classifier().run()
