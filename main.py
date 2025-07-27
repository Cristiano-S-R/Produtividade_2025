import streamlit as st
import pandas as pd
from PIL import Image

logo = Image.open("logo_geriba.jpg")  # Substitua pelo seu caminho




st.markdown("""
            # Grupo GERIBA
            
            ## Análise padronizada
               Carregue uma base padrão e gere vários relatórios pré programada em um clique. Aumente sua produtividade e confiabilidade em seus dados.
           """)

# Carrega a imagem (de um arquivo local ou URL)


formulario = st.file_uploader(label="Carregue seu arquivo Excel :", type=['xlsx'])

if formulario:
    filtro_02 = st.expander('Análises', expanded=True)
    tema01, tema02 = filtro_02.tabs(['Evolução Faturamento', 'Evolução Cobertura'])
    df = pd.read_excel(formulario)
    df['data'] = pd.to_datetime(df['data'])
    df['Faturamento_Acumulado'] = df['Faturamento'].cumsum()

    tema01.line_chart(
    data=df,
    x='data',          # Coluna para o eixo X
    y='Faturamento_Acumulado'    # Coluna para o eixo Y
)



    tema02.bar_chart(df,
       x='Vendedor',      # Coluna para o eixo X
       y='Faturamento'              )
