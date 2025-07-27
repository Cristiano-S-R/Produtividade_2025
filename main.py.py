import streamlit as st
import pandas  as pd

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
