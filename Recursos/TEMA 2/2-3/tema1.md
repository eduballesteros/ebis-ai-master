# 💡 Introducción a la Inteligencia Artificial Generativa (GenAI)

## 1. Introducción a la IA Generativa (GenAI) ✍️

La **Inteligencia Artificial Generativa (GenAI)** es una clase de modelos de IA cuyo objetivo principal no es clasificar o predecir un valor, sino **crear o generar** contenido nuevo y original que no existía antes.

* **¿Qué genera?** Puede generar textos, imágenes, videos, código de programación, música o incluso datos sintéticos.
* **Diferencia clave con IA Predictiva (Clásica):**
    * **Predictiva (ML/DL Clásico):** Responde a la pregunta: *"¿Qué es esto?"* (Clasificación) o *"¿Cuánto valdrá esto?"* (Regresión).
    * **Generativa (GenAI):** Responde a la pregunta: *"Crea algo que se parezca a esto."*

***

## 2. Tipos de IA Generativa (Modelos Fundamentales) 🧱

Los modelos generativos se basan en varias arquitecturas clave, siendo las más destacadas:

### A. Modelos Basados en Transformadores (Transformers y LLMs)

Estos modelos son la base de los **Grandes Modelos de Lenguaje (LLMs)** como GPT y son excelentes para tareas secuenciales como el lenguaje. Utilizan un mecanismo llamado **atención (Attention)**.

* **Mecanismo de Atención:** Permite al modelo ponderar la importancia de diferentes palabras de la entrada al procesar cada palabra de la salida. Es la clave para entender el contexto largo.
* **Fórmula del *Scaled Dot-Product Attention***:
    $$
    \text{Attention}(Q, K, V) = \text{softmax} \left( \frac{QK^T}{\sqrt{d_k}} \right) V
    $$
    Donde:
    * $Q$ (Query), $K$ (Key), $V$ (Value) son matrices derivadas de la entrada.
    * $d_k$ es la dimensión de las claves (Key) y se usa para escalar.
* **Tipos de Contenido:** Texto, Código, Conversación.

### B. Redes Generativas Antagónicas (GANs)

Las GANs son un par de redes neuronales que compiten entre sí para mejorar la calidad del contenido generado.

* **Componentes:**
    1.  **Generador ($G$):** Crea contenido (ej: una imagen falsa) a partir de un ruido aleatorio ($z$).
    2.  **Discriminador ($D$):** Intenta distinguir si el contenido es real (del conjunto de entrenamiento) o falso (creado por $G$).
* **Aprendizaje:** El Generador intenta "engañar" al Discriminador, y el Discriminador se vuelve mejor identificando falsificaciones. Este juego de suma cero es su función de coste:
    $$
    \min_{G} \max_{D} V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)} [\log D(x)] + \mathbb{E}_{z \sim p_{z}(z)} [\log (1 - D(G(z)))]
    $$
    * $D(x)$ es la probabilidad de que $x$ sea real.
    * $D(G(z))$ es la probabilidad de que la salida del Generador sea real.
* **Tipos de Contenido:** Imágenes realistas (**DeepFakes**), Video.
* **Ejemplo Gráfico (Estructura GAN):** 

### C. Modelos de Difusión (Diffusion Models)

Son la arquitectura de vanguardia, especialmente en la generación de imágenes.

* **Funcionamiento:**
    1.  **Fase Adelante (Forward):** Ruido gaussiano se agrega progresivamente a la imagen de entrenamiento hasta que solo queda ruido puro.
    2.  **Fase Reversa (Reverse):** El modelo aprende a *eliminar* el ruido progresivamente hasta reconstruir la imagen original, guiado por un *prompt* de texto.
* **Tipos de Contenido:** Imágenes de alta resolución (como las de DALL-E 3 o Midjourney), Música.

***

## 3. Casos de Uso de la IA Generativa 🚀

| Sector | Caso de Uso | Descripción |
| :--- | :--- | :--- |
| **Creatividad y Diseño** | Generación de Imágenes (Text-to-Image) | Crear un logotipo, un concepto artístico o un *background* para un videojuego a partir de una descripción de texto. |
| **Desarrollo de Software** | Completado de Código | Generar funciones o *snippets* de código en diferentes lenguajes (ej: Copilot). |
| **Marketing y Ventas** | Personalización de Contenido | Generar descripciones de productos, emails de marketing o publicaciones en redes sociales adaptadas a un cliente específico. |
| **Entretenimiento** | Creación de Mundos Virtuales | Generar texturas, objetos 3D o diálogos para personajes en videojuegos. |
| **Ciencia** | Descubrimiento de Fármacos | Generar la estructura de nuevas moléculas con propiedades deseadas. |

***

## 4. Aplicación Programática (APIs) 💻

La **Aplicación Programática** se refiere a cómo los desarrolladores interactúan y utilizan los modelos de IA Generativa en sus propias aplicaciones de software. Esto se realiza principalmente a través de **APIs (Interfaces de Programación de Aplicaciones)**.

* **¿Qué es una API?** Es un conjunto de reglas y protocolos que permite que un software se comunique con otro.
* **Funcionamiento con GenAI:** Un desarrollador envía una **petición HTTP** (ej: un *prompt* de texto) a la API del modelo (ej: OpenAI, Google Gemini). El servidor del modelo ejecuta la inferencia y devuelve la **respuesta generada** (texto, JSON, o un enlace a la imagen).
* **Ejemplo (Pseudocódigo de una Inferencia de Texto):**

```python
# Definición de la función de la API
def generar_texto(prompt, modelo="GPT-4"):
    # Envía el prompt a la API
    respuesta = API_Call(modelo, prompt)
    
    # Recibe y devuelve el texto generado
    return respuesta.texto_generado
    
# Aplicación
prompt_usuario = "Escribe un haiku sobre la luna y el código."
texto_generado = generar_texto(prompt_usuario)
print(texto_generado)