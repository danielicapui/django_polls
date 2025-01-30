import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from telegram.ext.filters import TEXT
from .models import ChatMessage
from decouple import config
# config de loggin
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# init de bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Olá! Como posso ajudar hoje.')

# Função para responder às mensagens
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    bot_response = f'Você disse: {user_message}'
    
    # Salvar a mensagem e a resposta no banco de dados
    ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)
    
    await update.message.reply_text(bot_response)

def main() -> None:
    # digite o token do bot do telegram
    telegram_token = config('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(telegram_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(TEXT & ~CommandHandler, echo))

    application.run_polling()

if __name__ == '__main__':
    main()
