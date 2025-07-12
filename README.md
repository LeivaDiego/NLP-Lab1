# Laboratorio 1: Eliza

**Universidad del Valle de Guatemala**  
**Facultad de Ingeniería**  
**Departamento de Ciencias de la Computación**  
**Procesamiento de Lenguaje Natural**

## Autor

Diego Leiva - 21752

## ELIZA miniChatbot

Este es un chatbot de consola inspirado en ELIZA, desarrollado en Python como práctica de procesamiento de lenguaje natural (NLP). ELIZA simula una conversación con una "terapeuta" básica, reconociendo ciertos patrones en las frases del usuario y respondiendo con frases predefinidas.

### Tabla de Contenidos

- [Requisitos](#requisitos)
- [Instalación](#instalación)
  - [1. Clona el repositorio](#1-clona-el-repositorio)
  - [2. Crea y activa el entorno conda](#2-crea-y-activa-el-entorno-conda)
  - [3. Instala las dependencias](#3-instala-las-dependencias)
- [Cómo ejecutar ELIZA](#cómo-ejecutar-eliza)
- [Patrones de conversación reconocidos](#patrones-de-conversación-reconocidos)
- [Ejemplo de conversación](#ejemplo-de-conversación)
- [Reflexión de Errores ortográficos](#reflexión-de-errores-ortográficos)

### Requisitos

- Python 3.8 o superior
- Conda (recomendado)
- Sistema operativo: Windows, macOS o Linux

### Instalación

#### 1. Clona el repositorio

```bash
git clone https://github.com/LeivaDiego/NLP-Lab1.git
cd eliza-chatbot
```

#### 2. Crea y activa el entorno conda

```bash
conda create -n eliza python=3.12
conda activate eliza
```

#### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### Cómo ejecutar ELIZA

Ejecuta el chatbot desde la carpeta raíz del proyecto:

```bash
python -m src.main
```

El chatbot mostrará un banner ASCII al iniciar y responderá según lo que digas.

```text
    ________    _________   ___                 _       _ ____        __
   / ____/ /   /  _/__  /  /   |     ____ ___  (_)___  (_) __ )____  / /_
  / __/ / /    / /   / /  / /| |    / __ `__ \/ / __ \/ / __  / __ \/ __/
 / /___/ /____/ /   / /__/ ___ |   / / / / / / / / / / / /_/ / /_/ / /_
/_____/_____/___/  /____/_/  |_|  /_/ /_/ /_/_/_/ /_/_/_____/\____/\__/

```

### Patrones de conversación reconocidos

| Tipo de entrada            | Ejemplo                                      | Respuesta esperada                              |
| -------------------------- | -------------------------------------------- | ----------------------------------------------- |
| **Saludo**                 | "Hola", "Qué tal", "Buenos días"             | Saludo de bienvenida                            |
| **Despedida**              | "Adiós", "Hasta luego", "Bye"                | Cierre de conversación                          |
| **Ofensas**                | "tonta", "idiota", "estúpida"                | "No me trates así."                             |
| **Mención del bot**        | "Eliza"                                      | "Hola, ¿cómo estás?"                            |
| **Estado emocional**       | "Me siento cansado", "Estoy triste"          | Preguntas sobre el estado emocional             |
| **Poseer algo**            | "Mi familia", "Mi perro"                     | Preguntas sobre eso que posees                  |
| **Trabajo difícil**        | "Mi trabajo es difícil", "trabajo estresa"   | Pregunta sobre el entorno laboral               |
| **Estudios o universidad** | "La universidad me agota", "clases estresan" | Pregunta sobre carga académica                  |
| **Gustos o intereses**     | "Me gusta dibujar", "amo leer"               | Pregunta sobre tus intereses                    |
| **Preguntas del usuario**  | "¿Qué opinas?", "¿Debería seguir?"           | Respuesta reflexiva                             |
| **Texto no reconocido**    | Cualquier otro texto                         | Respuesta neutra (ej: “No puedo comprender...”) |

### Ejemplo de conversación

```text
> hola
¡Hola! ¿Cómo te sientes hoy?

> me siento confundido
¿Por qué te sientes confundido?

> adios
Ha sido un gusto hablar contigo. ¡Hasta luego!
```

## Reflexión de Errores ortográficos

**¿El bot funciona con errores ortográficos?**

Actualmente, el bot **no reconoce entradas con errores ortográficos**. Si el usuario escribe mal una palabra clave (por ejemplo, “holaaa” en lugar de “hola” o “me sientto” en lugar de “me siento”), el patrón no coincide y ELIZA responde con un mensaje neutro como “No puedo comprender tu comentario”.

**¿Qué soluciones posibles propones?**

Algunas posibles soluciones para que el bot sea más tolerante a errores ortográficos son:

1. **Uso de NLP más avanzado**
   Sustituir las expresiones regulares por modelos de lenguaje más robustos (como `spaCy` o modelos de clasificación con `transformers`) para interpretar la intención del usuario, incluso si hay errores.

2. **Ampliar los patrones con variantes comunes**
   Incluir variantes típicas de errores ortográficos en los patrones manualmente, aunque esta opción es menos escalable.
