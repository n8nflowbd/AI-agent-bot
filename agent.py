import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("❌ TOKEN missing")
    exit()

async def start(update, context):
    await update.message.reply_text("✅ Bot working!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("🚀 Bot started")
app.run_polling()
