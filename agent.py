import os
from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("8624798446:AAGwnO8Z_tBK4FySWX1KGBw9_FQK_89vyo0")

# Start command
async def start(update, context):
    keyboard = [["📅 Appointment", "📞 Contact"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "👋 Welcome!\nChoose an option:",
        reply_markup=reply_markup
    )

# Message handler
async def message_handler(update, context):
    text = update.message.text.lower()

    if "appointment" in text:
        reply = "📅 Book Appointment:\n👉 https://tally.so/r/OD0W8A"

    elif "contact" in text:
        reply = "📞 Call Doctor:\n👉 9000000000"

    else:
        reply = "❗ Please click button:\n📅 Appointment\n📞 Contact"

    await update.message.reply_text(reply)

# Run bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

print("Bot started...")
app.run_polling()
