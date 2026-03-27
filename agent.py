import os
import logging
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq
from github import Github

# ── CONFIG ──────────────────────────────────────
TELEGRAM_TOKEN  = os.environ.get("TELEGRAM_TOKEN")
GROQ_API_KEY    = os.environ.get("GROQ_API_KEY")
GITHUB_TOKEN    = os.environ.get("GITHUB_TOKEN")
GITHUB_USERNAME = "n8nflowbd"
GITHUB_REPO     = "client-sites"
# ────────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 PSP AI Freelance Bot চালু!\n\n"
        "Website বানাতে লেখো:\n"
        "/generate [তোমার requirement]\n\n"
        "Example:\n"
        "/generate একটা restaurant website বানাও বাংলায়\n\n"
        "সব সাইট দেখতে: /list"
    )


async def generate_site(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ Requirement লিখতে হবে!\n"
            "Example: /generate একটা portfolio website বানাও"
        )
        return

    requirement = " ".join(context.args)
    msg = await update.message.reply_text("⚙️ কাজ শুরু হয়েছে...\n🤖 AI code বানাচ্ছে (30-60 sec)")

    try:
        groq_client = Groq(api_key=GROQ_API_KEY)
        prompt = f"""Create a complete beautiful professional single-page HTML website.

REQUIREMENT: {requirement}

RULES:
1. Single HTML file - CSS and JS must be inside HTML
2. Use Google Fonts
3. Modern responsive mobile-friendly design
4. Beautiful colors and animations
5. Professional looking
6. Footer must say "Powered by PSP Digital Services"
7. Return ONLY HTML code - no explanation no markdown no backticks
8. Start with <!DOCTYPE html>"""

        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4096,
            temperature=0.7,
        )
        html_code = response.choices[0].message.content.strip()

        if "```" in html_code:
            html_code = html_code.replace("```html", "").replace("```", "").strip()
        if "<!doctype" in html_code.lower():
            idx = html_code.lower().index("<!doctype")
            html_code = html_code[idx:]

        await msg.edit_text("📤 GitHub-এ push হচ্ছে...")

        g = Github(GITHUB_TOKEN)
        repo = g.get_user(GITHUB_USERNAME).get_repo(GITHUB_REPO)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"site_{timestamp}.html"

        repo.create_file(
            path=filename,
            message=f"[AUTO] {requirement[:60]}",
            content=html_code,
        )

        live_url = f"https://{GITHUB_USERNAME}.github.io/{GITHUB_REPO}/{filename}"

        await msg.edit_text(
            f"✅ কাজ সম্পন্ন!\n\n"
            f"🌐 Live Link:\n{live_url}\n\n"
            f"📋 Requirement:\n{requirement[:100]}\n\n"
            f"⚠️ Live হতে 1-2 মিনিট লাগবে।"
        )

    except Exception as e:
        logger.error(f"Error: {e}")
        await msg.edit_text(f"❌ Error হয়েছে:\n{str(e)}")


async def list_sites(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_user(GITHUB_USERNAME).get_repo(GITHUB_REPO)
        files = repo.get_contents("")
        sites = [f for f in files if f.name.startswith("site_") and f.name.endswith(".html")]

        if not sites:
            await update.message.reply_text("📂 এখনো কোনো site বানানো হয়নি।")
            return

        text = "📋 বানানো Websites:\n\n"
        for i, site in enumerate(sites[-10:], 1):
            url = f"https://{GITHUB_USERNAME}.github.io/{GITHUB_REPO}/{site.name}"
            text += f"{i}. {url}\n\n"

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Website বানাতে লিখো:\n/generate [requirement]\n\nসব সাইট: /list"
    )


def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN environment variable not set!")

    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("generate", generate_site))
    app.add_handler(CommandHandler("list", list_sites))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 PSP AI Freelance Bot চালু!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
