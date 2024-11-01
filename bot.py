import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Configura il logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Ciao! Benvenuto nel bot delle caramelle!')

# Comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Questi sono i comandi disponibili:\n/start - Avvia il bot\n/help - Mostra questo messaggio di aiuto')

async def main() -> None:
    # Inserisci il tuo token qui
    application = ApplicationBuilder().token("7681894111:AAFoXoWJYY44tNg-Gcbvo0bQETSmVLkMvt0").build()

    # Registrare i gestori di comandi
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Avvia il polling
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
