import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import gdown


st.set_page_config(layout="wide")

# ID do arquivo
file_id = "1LLsanCjUXpeGhujc9hZE40NOzMCkFxby"

# URL formatada para download direto
url = f"https://drive.google.com/uc?id={file_id}"

# Nome do arquivo local
output = "BR_Municipios_2024.zip"

# Baixar o arquivo
gdf = gdown.download(url, output, quiet=False)

st.sidebar.image("logo_agro.jpg", use_container_width=True)
# Lista de estados únicos
estados = sorted(list(gdf['NM_UF'].unique()))

# Agora o selectbox fica dentro do sidebar
# Remove Paraná e coloca no começo
estados.remove("Paraná")  # ou "Paraná", dependendo da sua coluna
estados = ["Paraná"] + estados

# Cria o selectbox
estado_selecionado = st.sidebar.selectbox(
    "Escolha um estado:",
    estados,
    index=0  # Paraná selecionado por padrão
)


# Filtra os dados geoespaciais pelo estado escolhido
gdf_estado = gdf[gdf['NM_UF'] == estado_selecionado]

# Centraliza o mapa na média de latitude e longitude do estado
centro = [gdf_estado.geometry.centroid.y.mean(), gdf_estado.geometry.centroid.x.mean()]

m = folium.Map(location=centro, zoom_start=7)

# Adiciona os municípios do estado
folium.GeoJson(
    gdf_estado,
    tooltip=folium.GeoJsonTooltip(fields=['NM_MUN'], aliases=['Município:']),
    style_function=lambda x: {
        'fillColor': 'none',   # sem preenchimento
        'color': 'green',      # cor da borda
        'weight': 1,           # espessura da linha (quanto menor, mais fino)
        'opacity': 0.6,       # transparência da borda
        'fillColor': 'lightgreen',
        'fillOpacity': 0.7

    }
).add_to(m)

# Folium_static com largura em pixels (ex.: 1200)
folium_static(m, width=1200, height=520)











