from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = "YOUR_TOKEN"

async def reply(update, context):
    await update.message.reply_text("Bot is running!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot started...")
app.run_polling()
