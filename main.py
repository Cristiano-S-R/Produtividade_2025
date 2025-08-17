import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import gdown


st.set_page_config(layout="wide")

import os

import gdown
import zipfile
import os
import geopandas as gpd

# ID do arquivo no Google Drive
file_id = "1LLsanCjUXpeGhujc9hZE40NOzMCkFxby"
url = f"https://drive.google.com/uc?export=download&id={file_id}"
output_zip = "BR_Municipios_2024.zip"
extracted_folder = "BR_Municipios_2024_folder"

# Baixar do Drive
if not os.path.exists(output_zip):
    gdown.download(url, output_zip, quiet=False)

# Extrair zip
if not os.path.exists(extracted_folder):
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder)

# Listar arquivos extraídos para encontrar o .shp
shp_files = [f for f in os.listdir(extracted_folder) if f.endswith(".shp")]
if not shp_files:
    raise FileNotFoundError("Nenhum arquivo .shp encontrado no zip extraído.")

shp_path = os.path.join(extracted_folder, shp_files[0])

# Ler shapefile
gdf = gpd.read_file(shp_path)
print(gdf.head())


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

















