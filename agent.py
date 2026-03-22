import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("🤖 Doctor Bot Ready!\nType: appointment / contact")

async def message_handler(update, context):
    text = update.message.text.lower()

    if "appointment" in text:
        reply = "🩺 Book Appointment:\n👉 https://tally.so/r/OD0W8A
    elif "contact" in text:
        reply = "📞 Call Doctor: 9XXXXXXXXX"
    else:
        reply = "Type: appointment / contact"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

print("Bot started...")
app.run_polling()
if "appointment" in text:
    reply = "📅 Book Appointment:\n👉 https://tally.so/r/0D0W8A"

elif "contact" in text:
    reply = "📞 Call Doctor: 9000000000"

else:
    reply = "Type: appointment / contact"
