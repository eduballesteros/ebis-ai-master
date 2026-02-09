from google import genai
import streamlit as st
import os

st.title('Mi primera aplicacion de GenAI')

# TODO: Genera una Service Account para autenticar las llamadas
# - Google Cloud Project > IAM & Admin & Service Accounts
# - Crear Service Account
# - Asignar el rol: Usuario de Vertex AI (Vertex AI User)
# - Descargar el JSON de credenciales y añadirlo al proyecto
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_sa.json"

client = genai.Client(
    vertexai=True,
    project="streamlit-ebis",
    location="us-central1"
)

# Si tienes una API Key de Google AI Studio, la puedes utilizar
# en lugar de la Service Account
# client = genai.Client(api_key='AIzaSyC51oIPclzKZdbyxQ-TZxzyXP8DJpOvvHo', vertexai=False)

# Instancia el modelo de gemini-2.0-flash 
gemini_model = 'gemini-2.5-flash'

# TODO: Añadir un componente st.text_area para introducir el prompt
prompt = st.text_area("Introduce tu prompt aquí:")



# Añadimos un boton para enviar el prompt a Gemini y obtener la respuesta
if st.button("Generate response"):
    with st.spinner("Waiting for a response..."):
        # TODO: Realizar la petición client.models.generate_content
        response = client.models.generate_content(
            model=gemini_model,
            contents=prompt
        )
        # TODO: Escribir la respuesta (response.text) en un componente st.write
        st.write(response.text)

