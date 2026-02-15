from typing import List
from dataclasses import dataclass


@dataclass
class ModelInfo:
    """    
    Attributes:
        id: Identificador del modelo en la API de Gemini
        name: Nombre legible para mostrar al usuario
        input_price: Precio por millón de tokens de entrada (USD)
        output_price: Precio por millón de tokens de salida (USD)
        max_tokens: Máximo de tokens que soporta el modelo
        description: Descripción breve del modelo
    """
    
    id: str
    name: str
    input_price: float  # USD per 1M tokens
    output_price: float  # USD per 1M tokens
    max_tokens: int
    description: str


class ModelCatalog:
    """Catálogo de modelos Gemini disponibles."""
    
    # Precios de Google Gemini (actualizados febrero 2026)
    MODELS = [
        ModelInfo(
            id="gemini-2.0-flash",
            name="Gemini 2.0 Flash",
            input_price=0.075,
            output_price=0.30,
            max_tokens=1_048_576,  # 1M tokens
            description="Rápido y versátil - RECOMENDADO"
        ),
        ModelInfo(
            id="gemini-2.5-flash",
            name="Gemini 2.5 Flash",
            input_price=0.075,
            output_price=0.30,
            max_tokens=1_048_576,  # 1M tokens
            description="Versión estable más reciente de Flash"
        ),
        ModelInfo(
            id="gemini-2.5-pro",
            name="Gemini 2.5 Pro",
            input_price=1.25,
            output_price=5.00,
            max_tokens=2_097_152,  # 2M tokens
            description="Máxima capacidad para tareas complejas"
        ),
        ModelInfo(
            id="gemini-flash-latest",
            name="Gemini Flash Latest",
            input_price=0.075,
            output_price=0.30,
            max_tokens=1_048_576,
            description="Última versión de Flash (auto-actualizado)"
        ),
        ModelInfo(
            id="gemini-pro-latest",
            name="Gemini Pro Latest",
            input_price=1.25,
            output_price=5.00,
            max_tokens=2_097_152,
            description="Última versión de Pro (auto-actualizado)"
        ),
    ]
    
    @classmethod
    def get_all_models(cls) -> List[ModelInfo]:
        """
        Retorna lista de todos los modelos disponibles.
        
        Returns:
            Lista de objetos ModelInfo
        """
        return cls.MODELS
    
    @classmethod
    def get_model_by_id(cls, model_id: str) -> ModelInfo:
        """
        Obtiene información de un modelo por su ID.
        
        Args:
            model_id: ID del modelo (ej: "gemini-1.5-flash")
            
        Returns:
            ModelInfo del modelo solicitado
            
        Raises:
            ValueError: Si el modelo no existe en el catálogo
        """
        for model in cls.MODELS:
            if model.id == model_id:
                return model
        raise ValueError(f"Modelo '{model_id}' no encontrado en el catálogo")
    
    @classmethod
    def calculate_input_cost(cls, model_id: str, tokens: int) -> float:
        """
        Calcula el coste de entrada para un modelo y número de tokens.
        
        Args:
            model_id: ID del modelo
            tokens: Número de tokens de entrada
            
        Returns:
            Coste en USD (0.0 para modelos gratis)
            
        Example:
            >>> ModelCatalog.calculate_input_cost("gemini-1.5-flash", 1000)
            0.000075  # (1000 / 1_000_000) * 0.075
        """
        model = cls.get_model_by_id(model_id)
        return (tokens / 1_000_000) * model.input_price
    
    @classmethod
    def calculate_total_cost(cls, model_id: str, input_tokens: int, 
                           output_tokens: int) -> float:
        """
        Calcula el coste total (entrada + salida).
        
        Args:
            model_id: ID del modelo
            input_tokens: Tokens de entrada (prompt)
            output_tokens: Tokens de salida (respuesta)
            
        Returns:
            Coste total en USD
            
        Example:
            >>> ModelCatalog.calculate_total_cost("gemini-1.5-flash", 100, 500)
            0.000157  # (100/1M)*0.075 + (500/1M)*0.30
        """
        model = cls.get_model_by_id(model_id)
        input_cost = (input_tokens / 1_000_000) * model.input_price
        output_cost = (output_tokens / 1_000_000) * model.output_price
        return input_cost + output_cost