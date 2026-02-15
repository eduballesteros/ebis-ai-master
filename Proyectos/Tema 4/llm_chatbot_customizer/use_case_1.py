#!/usr/bin/env python3
"""
Caso Práctico 1: Consulta Personalizada a Modelos LLM

Script que permite al usuario personalizar consultas a modelos Gemini
optimizando costes y ajustando parámetros según necesidades.

Autor: Eduardo Ballesteros
Fecha: Febrero 2026
"""

import sys
from typing import Optional

from models.model_catalog import ModelCatalog
from models.llm_client import LLMClient
from utils.token_counter import TokenCounter
from utils.input_handler import InputHandler


def main():
    """Función principal que ejecuta el flujo completo de 6 pasos."""
    
    try:
        # Inicializar componentes
        input_handler = InputHandler()
        
        # ============================================================
        # PASO 1: Solicitar pregunta del usuario
        # ============================================================
        question = input_handler.get_user_question()
        
        # ============================================================
        # PASO 2: Calcular tokens de entrada
        # ============================================================
        # Nota: Para contar tokens necesitamos la API key configurada
        # Por ahora usamos estimación, luego Gemini nos dará el valor exacto
        try:
            token_counter = TokenCounter()
            input_tokens = token_counter.count_tokens(question)
        except Exception as e:
            # Si falla (ej: sin API key aún), usar estimación básica
            input_tokens = len(question) // 3
        
        print(f"\n Tokens de entrada (estimados): {input_tokens}")
        
        # ============================================================
        # PASO 3: Seleccionar modelo
        # ============================================================
        available_models = ModelCatalog.get_all_models()
        selected_model_id = input_handler.select_model(available_models, input_tokens)
        selected_model = ModelCatalog.get_model_by_id(selected_model_id)
        
        # ============================================================
        # PASO 4: Configurar límite de tokens de salida
        # ============================================================
        max_tokens = input_handler.get_max_tokens(selected_model.max_tokens)
        
        # ============================================================
        # PASO 5: Seleccionar nivel de creatividad
        # ============================================================
        temperature = input_handler.select_creativity()
        
        # ============================================================
        # PASO 6: Generar respuesta
        # ============================================================
        
        # Inicializar cliente LLM
        print("\n🔄 Conectando con Google Gemini...")
        llm_client = LLMClient()
        
        print(" Generando respuesta...\n")
        
        # Llamar a la API
        response, output_tokens = llm_client.generate_response(
            model_id=selected_model_id,
            prompt=question,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # Calcular coste total real
        # Nota: Gemini nos da los tokens exactos, así que recalculamos
        total_cost = ModelCatalog.calculate_total_cost(
            selected_model_id,
            input_tokens,  # Usamos la estimación inicial
            output_tokens   # Tokens reales de salida
        )
        
        # Mostrar respuesta formateada
        input_handler.display_response(
            response=response,
            model_name=selected_model.name,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_cost=total_cost
        )
        
        print("\n✅ Consulta completada exitosamente")
        
    except KeyboardInterrupt:
        # Usuario presionó Ctrl+C
        print("\n\n⚠️  Operación cancelada por el usuario")
        sys.exit(0)
    
    except ValueError as e:
        # Error de validación (API key inválida, parámetros incorrectos, etc.)
        print(f"\n❌ Error de validación: {e}")
        sys.exit(1)
    
    except Exception as e:
        # Cualquier otro error inesperado
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()