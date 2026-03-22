import os
from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    keyboard = [["📅 Book Appointment", "📞 Contact"], ["💊 Services"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Welcome 👋\nChoose option:",
        reply_markup=reply_markup
    )

async def handle_message(update, context):
    text = update.message.text.lower()

    if "appointment" in text:
        await update.message.reply_text("Send Name + Date + Time")

    elif "contact" in text:
        await update.message.reply_text("Call: 9876543210")

    elif "service" in text:
        await update.message.reply_text("We provide treatment")

    else:
        await update.message.reply_text("Type appointment/contact/service")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
