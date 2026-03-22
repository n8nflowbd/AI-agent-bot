import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")

# 👉 Start command
async def start(update, context):
    await update.message.reply_text(
        "👋 Doctor Bot Ready!\n\nType:\n👉 appointment\n👉 contact"
    )

# 👉 Message handler
async def message_handler(update, context):
    text = update.message.text.lower()

    if "appointment" in text:
        reply = "📅 Book Appointment:\n👉 https://tally.so/r/OD0W8A"

    elif "contact" in text:
        reply = "📞 Call Doctor: 9000000000"

    elif any(word in text for word in ["hi", "hello", "hey"]):
        reply = "👋 Welcome!\nType:\n👉 appointment\n👉 contact"

    else:
        reply = "❓ Please type:\n👉 appointment\n👉 contact"

    await update.message.reply_text(reply)

# 👉 App setup
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

print("✅ Bot started...")
app.run_polling()
