import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    print("❌ TELEGRAM_TOKEN not found!")
    exit()

async def reply(update, context):
    await update.message.reply_text("✅ Bot is working!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("🚀 Bot started...")
app.run_polling()
