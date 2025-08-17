import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd



st.set_page_config(layout="wide")
import gdown


# Seu link do Google Drive
url = 'https://drive.google.com/file/d/1u26SePxto9RDASJigq5AT6EBkowW75LY/view?usp=sharing'

# Extrair o ID do arquivo do URL
file_id = url.split('/')[-2]

# Definir o caminho de destino no seu computador (por exemplo, na mesma pasta do seu script)
local_path = './seu_arquivo.zip' # Altere o nome e a extensão conforme o seu arquivo

# Baixar o arquivo do Google Drive
gdown.download(f'https://drive.google.com/uc?id={file_id}', local_path, quiet=False)

# Agora, o arquivo está no seu computador.
# Use o geopandas para ler o arquivo a partir do caminho local
gdf = gpd.read_file(local_path)




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



























