import streamlit as st
import boto3
from dotenv import load_dotenv
import os
from PIL import Image

legend = {"jack_frost": "Jack Frost", "pixie": "Pixie", "decarabia": "Decarabia"}   
images_dict = {"Jack Frost": "img/Jack_Frost_sprite_small.png", "Pixie": "img/Pixie_sprite.png", "Decarabia": "img/Decarabia_sprite.png"}

class Classifier():
    def __init__(self):
        load_dotenv()
        self.s3 = None
        self.bucket = None
        self.env = os.getenv("env")

    def load_s3(self):
        self.s3 = boto3.client('s3',
                               region_name=os.getenv('AWS_REGION'),
                               aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                               aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        
        self.bucket = os.getenv("AWS_BUCKET_NAME")
        self.env = None

        return

    def run(self):
        st.title('Classificador de Demônios de Persona e Shin Megami Tensei')

        st.write('Este é um classificador de demônios de Persona e Shin Megami Tensei. Ele foi treinado para identificar Pixie, Jack Frost e Decarabia')
        st.write('Para usá-lo, basta fazer o upload de uma imagem de um desses demônios e clicar em "Classificar". Para melhores resultados, use imagens recortadas.')
        st.write('Escolha quantas imagens deseja classificar.')
        with st.form("my-form", clear_on_submit=True):
            image = st.file_uploader(f'Faça o upload da imagem', type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)
            col1, col2, col3, col4 = st.columns(4, gap="large")
            with col1:
                classify_button = st.form_submit_button('Classificar')
            with col4:    
                clear_button = st.form_submit_button('Limpar')

            if classify_button:
                if image != []:
                    with st.spinner('Classificando...'):
                        cols = st.columns(len(image))

                        for i in range(len(image)):
                            with cols[i]:
                                img = Image.open(image[i])
                                new_image = img.resize((150, 100))
                                st.image(new_image)
                                self.load_s3()
                                self.s3.put_object(Key=f"{image[i].name}", Body=image[i].read(), Bucket=os.getenv('AWS_BUCKET_NAME'))
                                result = response["body"]
                                response = {legend[k]: v for k, v in result.items()}
                                response = sorted(response.items(), key=lambda x: x[1], reverse=True)
                                for k, v in response:
                                    sprite = images_dict[k]
                                    st.markdown(f"![{k}]({sprite}) {v*100:.2f}%", unsafe_allow_html=True)

                else:
                    st.write('Por favor, faça o upload de uma imagem antes de clicar em "Classificar"')

            if clear_button:
                pass

if __name__ == '__main__':
    Classifier().run()
