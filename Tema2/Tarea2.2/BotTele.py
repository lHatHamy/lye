import logging
import re

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Expresión regular para detectar mensajes que contienen "Hola"
expresion_regular = re.compile(r"([0-9]*\s[G|g]uajolote[s]?\s(de|con)\s?(pollo|salchicha|pierna|queso)\s?(y|con)*(\squeso|\ssalchicha|\spierna|\spollo)*)", re.IGNORECASE)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"¡Hola! {user.mention_html()}! Soy RositaBot. Tomaré tu orden y se la dejaré al chef por ti.\n\nRecuerda" +
                                        " que tu pedido debe tomarse en minusculas y escribiendo correctamente los ingredientes (pollo, pierna, queso, salchicha).",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches the regular expression."""
    message_text = update.message.text
    if expresion_regular.search(message_text):
        await update.message.reply_text("¡tu orden fue tomada correctamente!")
    else:
        await update.message.reply_text("Tu orden no fue tomada correctamente. Intenta nuevamente")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token("7166970505:AAE8AOVDd5j8R_A9jFbJirV_F3_pMJc07K0").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()