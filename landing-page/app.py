import streamlit as st
from pages.classifier import Classifier

class App:
    def __init__(self):
        self.pages = {
            'Classifier': Classifier
        }

    def run(self):
        st.markdown("<style> ul {display: none;} </style>", unsafe_allow_html=True)
        logo_url = "landing-page/img/heehoo.png"
        st.sidebar.image(logo_url)
        st.sidebar.title('Classificador de Demônios')
        st.sidebar.markdown('Demônios suportados: <br> - Pixie <br> - Jack Frost <br> - Decarabia <br> - Angel', unsafe_allow_html=True)
        self.pages['Classifier']().run()

app = App()
app.run()