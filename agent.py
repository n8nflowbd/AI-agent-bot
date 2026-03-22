 async def start(update, context):
    await update.message.reply_text("🤖 Doctor Bot Ready!\nType: appointment / contact")

async def message_handler(update, context):
    text = update.message.text.lower()

    if "appointment" in text:
        reply = "🩺 Book Appointment:\n👉 https://tally.so/r/abc123"
    
    elif "contact" in text:
        reply = "📞 Call Doctor: 9XXXXXXXXX"
    
    else:
        reply = "Type: appointment / contact"

    await update.message.reply_text(reply)
