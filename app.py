import streamlit as st

def main():
    st.title('Classificador de Demônios de Persona e Shin Megami Tensei')

    st.write('Este é um classificador de demônios de Persona e Shin Megami Tensei. Ele foi treinado para identificar Pixie, Jack Frost e Decarabia')
    st.write('Para usá-lo, basta fazer o upload de uma imagem de um desses demônios e clicar em "Classificar". Para melhores resultados, use imagens recortadas.')
    image = st.file_uploader('Faça o upload de uma imagem', type=['png', 'jpg', 'jpeg'])
    classify_button = st.button('Classificar')

    if classify_button:
        if image is not None:
            st.write('Classificando...')
            st.image(image, width=300)
        else:
            st.write('Por favor, faça o upload de uma imagem antes de clicar em "Classificar"')

if __name__ == '__main__':
    main()