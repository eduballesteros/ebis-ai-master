# Caso Práctico 1: Consulta Personalizada a Modelos LLM

Sistema de consultas personalizadas a modelos Gemini que permite optimizar costes y ajustar parámetros según las necesidades del usuario.

## 📋 Descripción

Este proyecto implementa un sistema interactivo por consola que permite:

- **Selección de modelo**: Elegir entre 5 modelos Gemini según coste y capacidades
- **Cálculo de tokens**: Estimación precisa del coste antes de realizar la consulta
- **Control de salida**: Limitar tokens de respuesta para optimizar costes
- **Ajuste de creatividad**: Configurar el nivel de aleatoriedad en las respuestas (temperature)

## 🏗️ Arquitectura

### Estructura del Proyecto

```
llm_chatbot_customizer/
├── use_case_1.py              # Script principal (punto de entrada)
├── models/
│   ├── __init__.py
│   ├── model_catalog.py       # Catálogo de modelos y precios
│   └── llm_client.py          # Cliente para API de Gemini
├── utils/
│   ├── __init__.py
│   ├── token_counter.py       # Cálculo de tokens con Gemini API
│   └── input_handler.py       # Gestión de inputs de usuario
├── requirements.txt           # Dependencias del proyecto
├── .env.example              # Template de variables de entorno
├── .env                      # Variables de entorno (API key)
├── .gitignore
└── README.md
```

### Componentes Principales

#### 1. **ModelCatalog** (`models/model_catalog.py`)

- Mantiene catálogo actualizado de 5 modelos Gemini con precios
- Calcula costes estimados en base a tokens
- Proporciona información detallada de cada modelo

#### 2. **LLMClient** (`models/llm_client.py`)

- Gestiona la comunicación con Google Gemini API
- Maneja autenticación y configuración
- Procesa respuestas y extrae métricas (tokens, texto)

#### 3. **TokenCounter** (`utils/token_counter.py`)

- Utiliza Gemini API para conteo preciso de tokens
- Proporciona estimaciones como fallback
- Optimizado para español e inglés

#### 4. **InputHandler** (`utils/input_handler.py`)

- Gestiona toda la interacción con el usuario
- Valida inputs y maneja errores de forma robusta
- Presenta información de forma clara y estructurada

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Cuenta de Google con acceso a Gemini API

### Pasos de Instalación

1. **Clonar o descomprimir el proyecto**

   ```bash
   cd llm_chatbot_customizer
   ```

2. **Crear entorno virtual (recomendado)**

   ```bash
   python -m venv venv

   # Activar en Linux/Mac
   source venv/bin/activate

   # Activar en Windows
   venv\Scripts\activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**

   ```bash
   # Copiar template
   cp .env.example .env

   # Editar .env y añadir tu API key de Gemini
   # GEMINI_API_KEY=AIzaSy...
   ```

### Obtener API Key de Gemini

1. Visita [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Create API Key"
4. Copia la key (empieza con `AIza...`)
5. Pégala en tu archivo `.env`:
   ```bash
   GEMINI_API_KEY=AIzaSyD1234567890abcdefghijklmnopqrstuvwxyz
   ```

## 📖 Uso

### Ejecución Básica

```bash
python use_case_1.py
```

### Flujo de Ejecución

El script guiará al usuario a través de 6 pasos:

#### **1. Introduce tu pregunta**

Escribe la consulta que quieres hacer al modelo

#### **2. Visualiza tokens de entrada**

El sistema calcula y muestra cuántos tokens tiene tu pregunta

#### **3. Selecciona modelo**

Elige entre 5 modelos con diferentes características:

| Modelo               | Precio Input | Precio Output | Descripción               |
| -------------------- | ------------ | ------------- | ------------------------- |
| Gemini 2.0 Flash Exp | GRATIS       | GRATIS        | Experimental - muy rápido |
| Gemini 1.5 Flash     | $0.075/1M    | $0.30/1M      | Rápido y económico        |
| Gemini 1.5 Flash 8B  | $0.0375/1M   | $0.15/1M      | Muy económico             |
| Gemini 1.5 Pro       | $1.25/1M     | $5.00/1M      | Máxima capacidad          |
| Gemini Exp 1206      | GRATIS       | GRATIS        | Experimental avanzado     |

#### **4. Configura límite de tokens**

Define máximo de tokens en la respuesta (opcional)

#### **5. Ajusta creatividad**

Selecciona entre 5 niveles:

- **Muy preciso** (0.0) - Determinista
- **Preciso** (0.3) - Poco creativo
- **Equilibrado** (0.7) - Balance
- **Creativo** (1.0) - Variado
- **Muy creativo** (1.5) - Máxima variabilidad

#### **6. Recibe respuesta**

El sistema muestra la respuesta junto con métricas de uso y coste

---

### Ejemplo de Uso Completo

```
============================================================
CONSULTA PERSONALIZADA A MODELOS GEMINI
============================================================

Introduce tu pregunta: ¿Cuáles son las mejores prácticas para optimizar queries SQL?

📊 Tokens de entrada (estimados): 18

------------------------------------------------------------
MODELOS DISPONIBLES
------------------------------------------------------------

1. Gemini 2.0 Flash (Experimental)
   ID: gemini-2.0-flash-exp
   Descripción: Modelo experimental gratis - muy rápido
   Coste estimado de entrada: GRATIS ✨
   Precio: $0.0/1M tokens (in) | $0.0/1M tokens (out)

2. Gemini 1.5 Flash
   ID: gemini-1.5-flash
   Descripción: Rápido y económico para tareas cotidianas
   Coste estimado de entrada: $0.000001 USD
   Precio: $0.075/1M tokens (in) | $0.3/1M tokens (out)

[...más modelos...]

Selecciona un modelo (1-5): 2
✓ Modelo seleccionado: Gemini 1.5 Flash

------------------------------------------------------------
LÍMITE DE TOKENS DE SALIDA
------------------------------------------------------------
El modelo seleccionado soporta hasta 1,048,576 tokens.

Límite de tokens (vacío = sin límite): 500
✓ Límite establecido: 500 tokens

------------------------------------------------------------
NIVEL DE CREATIVIDAD
------------------------------------------------------------

1. Muy preciso (temperature: 0.0)
   Respuestas deterministas y consistentes

2. Preciso (temperature: 0.3)
   Ligeramente creativo pero enfocado

[...más niveles...]

Selecciona nivel de creatividad (1-5): 2
✓ Nivel seleccionado: Preciso (temperature: 0.3)

🔄 Conectando con Google Gemini...
🤖 Generando respuesta...

============================================================
RESPUESTA DEL MODELO
============================================================

Modelo: Gemini 1.5 Flash
Tokens de entrada: 18
Tokens de salida: 487
Coste total: $0.000147 USD

------------------------------------------------------------
[Respuesta del modelo aquí...]
------------------------------------------------------------

✅ Consulta completada exitosamente
```

## 🧪 Técnica Implementada

### Conteo de Tokens

Se utiliza la **API de Gemini** para conteo preciso de tokens:

```python
model = genai.GenerativeModel(model_name)
token_count = model.count_tokens(text)
num_tokens = token_count.total_tokens
```

**Ventajas:**

- Precisión exacta (usa el mismo tokenizador que el modelo)
- Sin dependencias externas
- Fallback a estimación si falla la API

### Gestión de API

Patrón **Cliente** para encapsular la lógica de comunicación:

```python
import google.generativeai as genai

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_id)

response = model.generate_content(
    prompt,
    generation_config={
        "temperature": temperature,
        "max_output_tokens": max_tokens
    }
)
```

### Manejo de Errores

Implementación robusta con múltiples niveles:

```python
try:
    # Código principal
except KeyboardInterrupt:
    # Usuario cancela (Ctrl+C)
except ValueError:
    # Error de validación
except Exception:
    # Cualquier otro error
```

### Programación Orientada a Objetos

Clases especializadas para cada responsabilidad:

- `ModelCatalog`: Gestión de modelos y precios
- `LLMClient`: Cliente de API
- `TokenCounter`: Conteo de tokens
- `InputHandler`: Interfaz de usuario
- `ModelInfo`: Dataclass para datos de modelos

## 💰 Estimación de Costes

Los precios mostrados son de febrero 2026 (verificar en [Google AI Pricing](https://ai.google.dev/pricing)).

**Ejemplo de cálculo:**

- Pregunta: 18 tokens
- Respuesta: 500 tokens
- Modelo: Gemini 1.5 Flash

```
Coste entrada = (18 / 1,000,000) × $0.075 = $0.00000135
Coste salida = (500 / 1,000,000) × $0.30 = $0.00015
Total = $0.00015135 USD
```

**Modelos GRATIS:**

- Gemini 2.0 Flash Exp
- Gemini Exp 1206

## 🐛 Troubleshooting

### Error: "No module named 'google.generativeai'"

```bash
pip install -r requirements.txt
```


### Error: "API key not valid"

Tu API key no es válida o ha expirado. Genera una nueva en [Google AI Studio](https://aistudio.google.com/app/apikey).

### Tokens diferentes del esperado

El conteo es preciso cuando usa la API. La estimación inicial (paso 2) puede variar.

## 📚 Dependencias

- **google-generativeai** (>=0.3.0): SDK oficial de Google Gemini
- **python-dotenv** (>=1.0.0): Gestión de variables de entorno


## 👤 Autor

**Eduardo Ballesteros**

- Desarrollador Backend (Java/Spring Boot)
- Máster en IA Generative Solutions Engineering
- [Portfolio](https://www.eduballesteros.es)


