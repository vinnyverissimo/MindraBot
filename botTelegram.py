import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram.constants import ChatAction
from config import TELEGRAM_TOKEN
from indexing import cria_indice, busca_contexto
from chat_engine import resposta_bot
import re

indice = cria_indice()


async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="MindraBot <b>online</b>!", parse_mode="HTML")


async def echo(update, context):
    user_message = update.message.text
    chat_id = update.effective_chat.id

    async def keep_typing():
        while not typing_done.is_set():
            await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
            # Telegram recomenda reenviar a cada 4-5 segundos
            await asyncio.sleep(3)

    typing_done = asyncio.Event()
    typing_task = asyncio.create_task(keep_typing())

    try:
        contexto = busca_contexto(indice, user_message)
        resposta = await asyncio.to_thread(resposta_bot, user_message, contexto)
    finally:
        typing_done.set()
        await typing_task

    resposta = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", resposta)

    await context.bot.send_message(chat_id=chat_id, text=resposta, parse_mode="HTML")


def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(
        filters.TEXT & (~filters.COMMAND), echo))
    application.run_polling()


if __name__ == '__main__':
    main()
