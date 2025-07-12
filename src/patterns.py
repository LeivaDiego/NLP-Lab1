import re

# Saludos
GREETING_PATTERNS = [
    r"\b(hola|holi|que tal|buenos dias|buenas tardes)\b",
]

# Despedidas
GOODBYE_PATTERNS = [
    r"\b(adios|hasta luego|chao|bye)\b",
]

# Ofensas
OFFENSIVE_PATTERN = re.compile(r"\b(tonta|estupida|idiota|tonto|inutil)\b", re.IGNORECASE)

# Nombre del bot
NAME_PATTERN = re.compile(r"\b(eliza)\b", re.IGNORECASE)

# Patrones de conversación
CONVERSATION_PATTERNS = [
    # Preguntas sobre sentimientos
    (re.compile(r"\bme siento (.*)", re.IGNORECASE),
     ["¿Por qué te sientes {0}?", 
      "¿Desde cuándo te sientes {0}?",
      "¿Cómo puedo ayudarte a sentirte mejor?"]),

    # Preguntas sobre el estado de ánimo
    (re.compile(r"\bestoy (.*)", re.IGNORECASE),
     ["¿Desde cuándo estás {0}?", 
      "¿Qué te hace sentir {0}?",
      "¿Qué te gustaría cambiar para sentirte mejor?"]),

    # Preguntas sobre la vida
    (re.compile(r"\bmi (\w+)\b", re.IGNORECASE),
     ["Cuéntame más sobre tu {0}.", 
      "¿Cómo te afecta tu {0}?",
      "¿Qué te gustaría mejorar en tu {0}?"]),

    # Preguntas sobre el trabajo
    (re.compile(r"\btrabajo\b.*\b(estresa|dificil|duro)\b", re.IGNORECASE),
     ["El trabajo puede ser duro. ¿Cómo lo manejas?", 
      "¿Te gustaría cambiar de trabajo?",
      "¿Hay algún aspecto que te inquieta de tu trabajo?"]),

    # Preguntas de opinión
    (re.compile(r".*\?\s*$", re.IGNORECASE),
     ["¿Qué opinas tú?", 
      "¿Por qué lo preguntas?",
      "Eso suena interesante. ¿Qué piensas al respecto?"]),

    # Preguntas sobre la universidad
     (re.compile(r"\b(estudio|universidad|clases|tareas)\b.*\b(estres|cansad[oa]|agotad[oa]|dificil)\b", re.IGNORECASE),
      ["La universidad puede ser demandante. ¿Qué es lo que más te estresa?",
       "¿Crees que estás manejando bien tus clases?",
       "A veces el cansancio académico puede afectarnos emocionalmente."]),

    # Preguntas sobre gustos
    (re.compile(r"\b(me gusta|me encanta|amo|disfruto)\b (.*)", re.IGNORECASE),
     ["¡Qué bien que te guste {1}! ¿Por qué te gusta tanto?",
      "Disfrutar de {1} suena genial. ¿Lo haces a menudo?",
      "¿Desde cuándo te gusta {1}?"]),
]

NEUTRAL_RESPONSES = [
    "No puedo comprender tu comentario.",
    "¿Podrías explicarlo de otra manera?",
    "No estoy segura de entender lo que dices.",
]
