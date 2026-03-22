from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "YOUR_TOKEN"

# Start menu
async def start(update, context):
    keyboard = [["📅 Book Appointment", "📞 Contact"], ["💊 Services"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Welcome Doctor Clinic 👋\nChoose option:",
        reply_markup=reply_markup
    )

# Handle messages
async def handle_message(update, context):
    text = update.message.text.lower()

    if "appointment" in text or "book" in text:
        await update.message.reply_text(
            "📅 Appointment booking:\nPlease send:\nName + Date + Time"
        )

    elif "contact" in text:
        await update.message.reply_text("📞 Call: 9876543210")

    elif "service" in text:
        await update.message.reply_text("💊 We provide diabetes & cardio treatment")

    else:
        await update.message.reply_text("❓ Please choose from menu or type 'appointment'")

# App setup
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot started...")
app.run_polling()
