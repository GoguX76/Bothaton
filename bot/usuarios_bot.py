import telebot as tl #Importo la libreria para manejar al bot de Telegram.
from config import TELEGRAM_TOKEN

usuarios_bot = tl.TeleBot(TELEGRAM_TOKEN) #Creo el bot mediante el token que Telegram te da al crea el bot.

#Función que se ejecuta al momento que el usuario escriba el comando 'start' y muestra el mensaje el pantalla descrito.
@usuarios_bot.message_handler(commands=['start'])
def start(message):
    usuarios_bot.reply_to(
        message,
        "¡Hola!\n\n"
        "Soy un bot para gestionar los usuarios presentes en el sistema\n"
        "Usa /help para ver los comandos disponibles"
    )

#Función que se ejecuta al momento que el usuario escriba el comando 'help', que le da orientación al usuario de que hacer.
@usuarios_bot.message_handler(commands=['help'])
def help_command(message):
    usuarios_bot.reply_to(
        message,
        "Comandos Disponibles\n\n"
        "/start - Iniciar el bot\n"
        "/help - Ver esta ayuda",
        parse_mode='Markdown'
    )

#Asegura de que el bot se ejecute solo en este archivo.
if __name__ == "__main__":
    print("Iniciando bot...")
    print("Bot iniciado correctamente")

    try:
        usuarios_bot.polling() #Mantiene constamente al bot escuchando para la entrada de nuevos mensajes.
    except KeyboardInterrupt: #Si el usuario interrumpe la respuesta del bot
        print("Bot detenido por el usuario")
    except Exception as e:
        print(f"Error: {e}") #Si es otro error, se lo muestra al usuario mediante consola.