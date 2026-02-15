from google import genai
from google.genai import types


class TokenCounter:
    """Contador de tokens para textos usando Gemini."""
    
    def __init__(self, model_name: str = "gemini-2.0-flash", api_key: str = None):
        """
        Inicializa el contador de tokens.
        
        Args:
            model_name: Nombre del modelo a usar para contar tokens
            api_key: API key de Gemini (opcional, se lee de .env si no se proporciona)
        """
        self.model_name = model_name
        
        # Si no se proporciona API key, intentar obtenerla de variables de entorno
        if api_key is None:
            import os
            from dotenv import load_dotenv
            load_dotenv()
            api_key = os.getenv("GEMINI_API_KEY")
        
        if api_key:
            self.client = genai.Client(api_key=api_key)
        else:
            self.client = None
    
    def count_tokens(self, text: str) -> int:
        """
        Cuenta el número de tokens en un texto usando la API de Gemini.
        
        Args:
            text: Texto a analizar
            
        Returns:
            Número de tokens
            
        Raises:
            ValueError: Si el texto está vacío
            Exception: Si hay error en la API
        """
        if not text or not text.strip():
            return 0
        
        try:
            if self.client is None:
                # Si no hay cliente configurado, usar estimación
                return self._estimate_tokens(text)
            
            # Usar el nuevo método de la API para contar tokens
            response = self.client.models.count_tokens(
                model=self.model_name,
                contents=text
            )
            
            # La API devuelve el conteo total de tokens
            return response.total_tokens
            
        except Exception as e:
            # Si falla la API, usar estimación
            print(f"⚠️  No se pudo contar tokens vía API, usando estimación: {e}")
            return self._estimate_tokens(text)
    
    def _estimate_tokens(self, text: str) -> int:
        """
        Estimación rápida de tokens sin usar la API.
        
        Aproximación conservadora:
        - 1 token ≈ 4 caracteres en inglés
        - 1 token ≈ 2-3 caracteres en español
        
        Args:
            text: Texto a analizar
            
        Returns:
            Estimación de número de tokens
        """
        if not text:
            return 0
        
        # Usar estimación conservadora (1 token cada 3 caracteres)
        estimated = len(text) // 3
        
        # Mínimo 1 token si hay texto
        return max(1, estimated)