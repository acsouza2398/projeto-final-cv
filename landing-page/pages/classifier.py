import streamlit as st
import requests
from dotenv import load_dotenv
import os
import io
from PIL import Image
import base64
from pathlib import Path

legend = {"jack_frost": "Jack Frost", "pixie": "Pixie", "decarabia": "Decarabia"}   
images_dict = {"Jack Frost": "img/Jack_Frost_sprite_small.png", "Pixie": "img/Pixie_sprite.png", "Decarabia": "img/Decarabia_sprite.png"}

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

class Classifier():
    def __init__(self):
        load_dotenv()
        self.env = os.getenv("env")
        self.api_url = os.getenv("API_URL")

    def start(self):
        img = Image.open("img/heehoo.png")
        buffered = io.BytesIO()
        img.save(buffered, format="png")
        image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

        payload = {'image_data': image_base64}
        response = requests.post(self.api_url, json=payload)

    def run(self):
        self.start()
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
                    with st.spinner('Classificando... Hee Ho!'):
                        cols = st.columns(len(image))

                        for i in range(len(image)):
                            with cols[i]:
                                img = Image.open(image[i])
                                new_image = img.resize((150, 100))
                                st.image(new_image)

                                buffered = io.BytesIO()
                                print(image[i].type.split('/')[1])
                                img.save(buffered, format=image[i].type.split('/')[1])
                                image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

                                payload = {'image_data': image_base64}
                                response = requests.post(self.api_url, json=payload)

                                print(response.json())
                                print(response.status_code)

                                if response.status_code == 200:
                                    result = response.json()
                                    predictions = result["predictions"]
                                    print(f"Predictions: {predictions}")
                                    response = {legend[k]: v for k, v in predictions.items()}
                                    response = sorted(response.items(), key=lambda x: x[1], reverse=True)
                                    for k, v in response:
                                        sprite = images_dict[k]
                                        st.markdown(f"<img src='data:image/png;base64,{img_to_bytes(sprite)}' class='img-fluid'> {k}: {v*100:.2f}%", unsafe_allow_html=True)
                                else:
                                    st.error('Erro ao classificar a imagem.')

                else:
                    st.write('Por favor, faça o upload de uma imagem antes de clicar em "Classificar"')

            if clear_button:
                pass

if __name__ == '__main__':
    Classifier().run()
