import os
import uuid
import streamlit as st

from google import genai
from google.genai import types
from PIL import Image


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_sa.json"

client = genai.Client(
    vertexai=True,
    project="streamlit-ebis-1770468023",  # TODO: Rellenar cn tu PROJECT_ID
    location="us-central1"
)


# ------ Streamlit UX/UI ------

st.title("Prompt parametrizado")

# Componente para escribir el prompt
prompt = st.text_area("Prompt", value="Una foto realista tomada desde lejos y con un gran angular de un monumento o lugar representativo de ")
cities = ["Paris", "Berlin", "Madrid"]

# Streamlit component para listar las ciudades de las que dinámicamente vamos a generar imágenes
st.subheader("Ciudades:")
for ciudad in cities:
  st.write(f"- {ciudad}")


if st.button("Generate Image"):
  with st.spinner("Generating image..."):
    # TODO: Iterar sobre cada una de las ciudades (for)
    for ciudad in cities:
        # TODO: para cada ciudad, parametrizar el prompt
        prompt_paremetrizado = f"{prompt} {ciudad}"
        response = client.models.generate_images(
            model='imagen-3.0-generate-001',
            prompt=prompt_paremetrizado,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
                safety_filter_level="block_some",
                person_generation="allow_adult",
            )
        ) 
    # TODO: Añadir la imagen a un componente st.image
    imagen = response.generated_images[0].image
    st.image(
      imagen.image_bytes,
      caption=f"Imagen de {ciudad}",
      width="stretch"
    )
