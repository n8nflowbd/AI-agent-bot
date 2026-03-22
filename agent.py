import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from groq import Groq

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


client = Groq(api_key=GROQ_API_KEY)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    await update.message.reply_text("কাজ করছি...")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert web developer. Create complete single HTML file. Return only code."},
            {"role": "user", "content": user_msg}
        ]
    )
    reply = response.choices[0].message.content
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(reply)
    await update.message.reply_text("Done! Desktop-এ output.html দেখো!")

def main():
    print("Bot চালু হয়েছে!")
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == "__main__":
    main()