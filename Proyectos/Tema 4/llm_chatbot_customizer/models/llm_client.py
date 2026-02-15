import os
from typing import Optional, Tuple
from google import genai
from google.genai import types
from dotenv import load_dotenv


class LLMClient:
    """Cliente para realizar consultas a modelos Gemini de Google."""
    
    def __init__(self):
        """
        Inicializa el cliente de Gemini.
        
        Raises:
            ValueError: Si no se encuentra la API key válida
        """
        # Cargar variables de entorno desde .env
        load_dotenv()
        
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key or api_key == "your_api_key_here":
            raise ValueError(
                "No se encontró GEMINI_API_KEY válida.\n"
                "Por favor:\n"
                "1. Copia .env.example a .env\n"
                "2. Añade tu API key de Google Gemini\n"
                "3. Obtén tu key en: https://aistudio.google.com/app/apikey"
            )
        
        try:
            # Configurar el cliente con la API key
            self.client = genai.Client(api_key=api_key)
        except Exception as e:
            raise ValueError(f"Error al configurar cliente de Gemini: {e}")
    
    def generate_response(
        self,
        model_id: str,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> Tuple[str, int]:
        """
        Genera una respuesta usando el modelo especificado.
        
        Args:
            model_id: ID del modelo a usar (ej: "gemini-1.5-flash")
            prompt: Pregunta/prompt del usuario
            temperature: Nivel de creatividad (0.0 - 2.0)
            max_tokens: Límite de tokens de salida (None = sin límite)
            
        Returns:
            Tupla (respuesta_texto, tokens_de_salida)
            
        Raises:
            ValueError: Si los parámetros son inválidos
            Exception: Si hay error en la API
        """
        # Validar temperatura
        if not 0.0 <= temperature <= 2.0:
            raise ValueError(
                f"Temperature debe estar entre 0.0 y 2.0, recibido: {temperature}"
            )
        
        # Validar max_tokens
        if max_tokens is not None and max_tokens <= 0:
            raise ValueError(f"max_tokens debe ser positivo, recibido: {max_tokens}")
        
        try:
            # Configurar parámetros de generación
            config = types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens if max_tokens is not None else None
            )
            
            # Generar respuesta usando la nueva API
            response = self.client.models.generate_content(
                model=model_id,
                contents=prompt,
                config=config
            )
            
            # Extraer el texto de la respuesta
            response_text = response.text
            
            # Extraer tokens de salida desde los metadatos de uso
            output_tokens = response.usage_metadata.candidates_token_count
            
            return response_text, output_tokens
            
        except AttributeError as e:
            # Error al acceder a atributos de la respuesta
            raise Exception(
                f"Error al procesar respuesta de Gemini: {e}\n"
                f"Posible respuesta bloqueada por filtros de seguridad."
            )
        
        except Exception as e:
            # Cualquier otro error de la API
            raise Exception(f"Error al generar respuesta con Gemini: {e}")
    
    def test_connection(self) -> bool:
        """
        Prueba la conexión con la API de Gemini.
        
        Returns:
            True si la conexión es exitosa, False en caso contrario
        """
        try:
            # Hacer una llamada mínima para verificar
            config = types.GenerateContentConfig(max_output_tokens=5)
            
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents="Di 'OK'",
                config=config
            )
            
            # Si llegamos aquí, la conexión funciona
            return True
            
        except Exception as e:
            print(f"❌ Error al probar conexión: {e}")
            return False