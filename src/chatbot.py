import random
from .patterns import (
    GREETING_PATTERNS, GOODBYE_PATTERNS,
    OFFENSIVE_PATTERN, NAME_PATTERN,
    CONVERSATION_PATTERNS, NEUTRAL_RESPONSES
)

from .utils import matches_any, normalize_text

class ElizaBot:
    def __init__(self):
        self.started = False

    def respond(self, user_input):
        # Normalizamos la entrada del usuario (sin tildes, minúsculas)
        norm_input = normalize_text(user_input)

        # Verificamos si ya se saludó
        if not self.started:
            if matches_any(norm_input, GREETING_PATTERNS):
                self.started = True
                return random.choice([
                    "¡Hola! ¿Cómo te sientes hoy?",
                    "Saludos, cuéntame lo que te pasa.",
                    "¡Qué gusto saludarte! ¿En qué puedo ayudarte?"
                ]), False
            else:
                return "Es importante iniciar una conversación con un saludo.", False

        # Verificamos si es una despedida
        if matches_any(norm_input, GOODBYE_PATTERNS):
            return "Ha sido un gusto hablar contigo. ¡Hasta luego!", True

        # Verificamos si el mensaje es ofensivo
        if OFFENSIVE_PATTERN.search(norm_input):
            return "No me trates así.", False

        # Verificamos si se menciona el nombre del bot
        if NAME_PATTERN.search(norm_input):
            return "Hola, ¿cómo estás?", False

        # Buscamos coincidencias con patrones de conversación
        for pattern, responses in CONVERSATION_PATTERNS:
            match = pattern.search(norm_input)
            if match:
                groups = [g.strip() for g in match.groups()]
                return random.choice(responses).format(*groups), False

        # Si nada coincide, damos una respuesta neutra
        return random.choice(NEUTRAL_RESPONSES), False
