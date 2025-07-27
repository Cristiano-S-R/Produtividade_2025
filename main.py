import streamlit as st
import pandas  as pd

import streamlit as st

st.markdown("---")
st.caption("© 2025 GERIBA - Todos os direitos reservados")

st.set_page_config(
    page_title="Título do Seu App",
    page_icon="🔒",
    layout="centered",  # ou "wide"
    initial_sidebar_state="collapsed",  # opcional: recolhe a sidebar
    menu_items={
        'Get Help': None,  # Remove link "Get Help"
        'Report a bug': None,  # Remove link "Report a bug"
        'About': None  # Remove seção "About"
    }
)

# Esconde o menu padrão e rodapé via CSS
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown("""
                 # Sistema de mapas 

                  Seja muito bem vindo a revoução




                    """
)

formulario = st.file_uploader(label="Carregue seu arquivo :",type=['xlsx'])


if formulario:
    filtro_01 = st.expander('Bloco 01')
    df = pd.read_excel(formulario)
    filtro_01.dataframe(df)

if formulario:
    filtro_02 = st.expander('Bloco 02')
    tema01,tema02 =filtro_02.tabs(['Tema 01','Tema 02'])
    df = pd.read_excel(formulario)
    tema01.line_chart(df)
    tema02.bar_chart(df)
