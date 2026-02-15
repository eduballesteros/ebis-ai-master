from typing import Optional, List
from models.model_catalog import ModelInfo


class InputHandler:
    """Manejador de entradas de usuario por consola."""
    
    # Niveles de creatividad (mapean a temperature en Gemini)
    CREATIVITY_LEVELS = [
        ("Muy preciso", 0.0, "Respuestas deterministas y consistentes"),
        ("Preciso", 0.3, "Ligeramente creativo pero enfocado"),
        ("Equilibrado", 0.7, "Balance entre creatividad y precisión"),
        ("Creativo", 1.0, "Respuestas variadas y originales"),
        ("Muy creativo", 1.5, "Máxima variabilidad y creatividad"),
    ]
    
    @staticmethod
    def get_user_question() -> str:
        """
        Solicita la pregunta del usuario.
        
        Returns:
            Pregunta del usuario (string no vacío)
        """
        print("\n" + "="*60)
        print("CONSULTA PERSONALIZADA A MODELOS GEMINI")
        print("="*60)
        print()
        
        while True:
            question = input("Introduce tu pregunta: ").strip()
            
            if not question:
                print("⚠️  La pregunta no puede estar vacía. Inténtalo de nuevo.")
                continue
            
            return question
    
    @staticmethod
    def select_model(models: List[ModelInfo], input_tokens: int) -> str:
        """
        Muestra menú de modelos y solicita selección.
        
        Args:
            models: Lista de modelos disponibles
            input_tokens: Número de tokens de la pregunta
            
        Returns:
            ID del modelo seleccionado
        """
        print("\n" + "-"*60)
        print("MODELOS DISPONIBLES")
        print("-"*60)
        
        for idx, model in enumerate(models, 1):
            from models.model_catalog import ModelCatalog
            cost = ModelCatalog.calculate_input_cost(model.id, input_tokens)
            
            print(f"\n{idx}. {model.name}")
            print(f"   ID: {model.id}")
            print(f"   Descripción: {model.description}")
            
            if cost == 0.0:
                print(f"   Coste estimado de entrada: GRATIS ✨")
            else:
                print(f"   Coste estimado de entrada: ${cost:.6f} USD")
            
            print(f"   Precio: ${model.input_price}/1M tokens (in) | "
                  f"${model.output_price}/1M tokens (out)")
        
        print("\n" + "-"*60)
        
        while True:
            try:
                selection = input(f"\nSelecciona un modelo (1-{len(models)}): ").strip()
                
                if not selection:
                    print("⚠️  Debes seleccionar un modelo.")
                    continue
                
                idx = int(selection)
                
                if 1 <= idx <= len(models):
                    selected_model = models[idx - 1]
                    print(f"✓ Modelo seleccionado: {selected_model.name}")
                    return selected_model.id
                else:
                    print(f"⚠️  Selección inválida. Debe estar entre 1 y {len(models)}.")
            
            except ValueError:
                print("⚠️  Por favor, introduce un número válido.")
    
    @staticmethod
    def get_max_tokens(model_max: int) -> Optional[int]:
        """
        Solicita límite de tokens de salida.
        
        Args:
            model_max: Máximo de tokens que soporta el modelo
            
        Returns:
            Límite de tokens o None (ilimitado)
        """
        print("\n" + "-"*60)
        print("LÍMITE DE TOKENS DE SALIDA")
        print("-"*60)
        print(f"El modelo seleccionado soporta hasta {model_max:,} tokens.")
        print("Puedes establecer un límite menor para controlar costes.")
        print("Deja vacío para no establecer límite.")
        
        while True:
            user_input = input(f"\nLímite de tokens (vacío = sin límite): ").strip()
            
            if not user_input:
                print("✓ Sin límite de tokens establecido")
                return None
            
            try:
                max_tokens = int(user_input)
                
                if max_tokens <= 0:
                    print("⚠️  El límite debe ser un número positivo.")
                    continue
                
                if max_tokens > model_max:
                    print(f"⚠️  El límite no puede exceder {model_max:,} tokens.")
                    continue
                
                print(f"✓ Límite establecido: {max_tokens:,} tokens")
                return max_tokens
            
            except ValueError:
                print("⚠️  Por favor, introduce un número válido.")
    
    @staticmethod
    def select_creativity() -> float:
        """
        Solicita nivel de creatividad.
        
        Returns:
            Valor de temperature (0.0 - 2.0)
        """
        print("\n" + "-"*60)
        print("NIVEL DE CREATIVIDAD")
        print("-"*60)
        
        levels = InputHandler.CREATIVITY_LEVELS
        
        for idx, (name, temp, desc) in enumerate(levels, 1):
            print(f"\n{idx}. {name} (temperature: {temp})")
            print(f"   {desc}")
        
        print("\n" + "-"*60)
        
        while True:
            try:
                selection = input(f"\nSelecciona nivel de creatividad (1-{len(levels)}): ").strip()
                
                if not selection:
                    print("⚠️  Debes seleccionar un nivel.")
                    continue
                
                idx = int(selection)
                
                if 1 <= idx <= len(levels):
                    name, temperature, _ = levels[idx - 1]
                    print(f"✓ Nivel seleccionado: {name} (temperature: {temperature})")
                    return temperature
                else:
                    print(f"⚠️  Selección inválida. Debe estar entre 1 y {len(levels)}.")
            
            except ValueError:
                print("⚠️  Por favor, introduce un número válido.")
    
    @staticmethod
    def display_response(response: str, model_name: str, 
                        input_tokens: int, output_tokens: int, 
                        total_cost: float):
        """
        Muestra la respuesta del modelo formateada.
        
        Args:
            response: Respuesta del modelo
            model_name: Nombre del modelo usado
            input_tokens: Tokens de entrada
            output_tokens: Tokens de salida
            total_cost: Coste total en USD
        """
        print("\n" + "="*60)
        print("RESPUESTA DEL MODELO")
        print("="*60)
        print(f"\nModelo: {model_name}")
        print(f"Tokens de entrada: {input_tokens:,}")
        print(f"Tokens de salida: {output_tokens:,}")
        
        if total_cost == 0.0:
            print(f"Coste total: GRATIS ✨")
        else:
            print(f"Coste total: ${total_cost:.6f} USD")
        
        print("\n" + "-"*60)
        print(response)
        print("-"*60)