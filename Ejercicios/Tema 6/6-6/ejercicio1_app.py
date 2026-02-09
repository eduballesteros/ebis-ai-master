import streamlit as st

st.title("Hola! 👋")
st.write("Esta es nuestra primera app en Streamlit.")
st.write("Vamos a ver algún componente.")

# 1) Tipos de texto
st.title("Tipos de texto")
st.header("Esto es un header")
st.subheader("Esto es un subheader")
st.write("Esto es texto normal")
st.caption("Esto es un caption")
# 2) Mensajes
st.header("Tipos de mensajes")
st.subheader('st.info')
st.info("Mensaje informativo")
st.subheader('st.success')
st.success("Mensaje de éxito")
st.subheader('st.warning')
st.warning("Mensaje de warning")
st.subheader('st.error')
st.error("Mensaje de error")
 
#3. Media - Imagen
st.header('Mostrar una imagen')
st.image('media/image.jpeg', caption='Una imagen', width=500)


# # 4. Media - Video
# st.header('Reproducir un video')
# video_file = open('media/train.mp4', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)


# # 5. Media - Audio
# st.header('Reproducir un audio')
# audio_file = open('media/audio.mp3', 'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/mp3')