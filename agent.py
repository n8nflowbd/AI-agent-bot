async def message_handler(update, context):
    text = update.message.text.lower()

    if "appointment" in text:
        reply = "📅 Book Appointment:\n👉 https://tally.so/r/OD0W8A"

    elif "contact" in text:
        reply = "📞 Call Doctor: 9000000000"

    elif "hi" in text or "hello" in text:
        reply = "👋 Welcome!\nType:\n👉 appointment\n👉 contact"

    else:
        reply = "❓ Type:\n👉 appointment\n👉 contact"

    await update.message.reply_text(reply)
