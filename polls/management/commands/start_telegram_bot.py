import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
from telegram.ext.filters import TEXT
from django.core.management.base import BaseCommand
from polls.models import ChatMessage
from decouple import config
from asgiref.sync import sync_to_async
#adição de transformers
from transformers import pipeline
class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **kwargs):
        # Função para iniciar o bot
        async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            await update.message.reply_text('Olá! Eu sou o seu chatbot.')

        # Função para responder às mensagens
        async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
            user_message = update.message.text
            bot_response = f'Você disse: {user_message}'
             # Respostas predefinidas para perguntas comuns
            predefined_responses = {
                "olá": "Olá! Como posso ajudar você hoje?",
                "como você está?": "Estou bem, obrigado por perguntar! E você?",
                "qual é o seu nome?": "Eu sou um chatbot criado para ajudar você.",
                "o que você pode fazer?": "Posso responder suas perguntas e ajudar com informações gerais."
            }
            # Verificar se a mensagem do usuário está nas respostas predefinidas
            bot_response = predefined_responses.get(user_message.lower())
            if not bot_response:
                ## Usar um modelo de NLP para gerar uma resposta
                #nlp = pipeline("conversational", model="microsoft/DialoGPT-medium")
                #conversation = nlp(user_message)
                #bot_response = conversation[0]['generated_text']
                ## Usar um modelo de geração de texto para criar uma resposta
                generator=pipeline("text-generation",model="pierreguillou/gpt2-small-portuguese")
                response=generator(user_message,max_length=50,num_return_sequences=1)
                bot_response=response[-0]['generated_text']
            # Salvar a mensagem e a resposta no banco de dados de forma assíncrona
            await sync_to_async(ChatMessage.objects.create)(user_message=user_message, bot_response=bot_response)
            
            await update.message.reply_text(bot_response)

        # Carregar o token do Telegram das variáveis de ambiente
        telegram_token = config('TELEGRAM_TOKEN')
        application = ApplicationBuilder().token(telegram_token).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(TEXT, echo))

        application.run_polling()
