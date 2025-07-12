from pyfiglet import Figlet
from .chatbot import ElizaBot

def main():
    f = Figlet(font='slant')
    print(f.renderText('ELIZA miniBot'))

    print("Escribe 'adios' para terminar la conversación.\n")

    bot = ElizaBot()

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nFinalizando conversación. ¡Cuídate!")
            break

        response, finished = bot.respond(user_input)
        print(response)

        if finished:
            break

if __name__ == "__main__":
    main()