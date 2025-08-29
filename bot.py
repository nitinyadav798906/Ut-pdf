import os
import requests
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, WORKER_URL

app = Client("utkarsh-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start(_, msg):
    await msg.reply_text("👋 Send me a Utkarsh PDF/Video URL using `/get <url>`")


@app.on_message(filters.command("get"))
async def get_file(_, msg):
    if len(msg.command) < 2:
        return await msg.reply_text("⚠️ Please provide a valid URL.\n\nExample: `/get https://apps-s3...pdf`")

    file_url = msg.command[1]
    proxy_url = WORKER_URL + file_url

    await msg.reply_text("📥 Downloading... Please wait!")

    try:
        r = requests.get(proxy_url, stream=True)
        filename = file_url.split("/")[-1]

        with open(filename, "wb") as f:
            for chunk in r.iter_content(1024 * 1024):
                if chunk:
                    f.write(chunk)

        await msg.reply_document(document=filename, caption="✅ Here is your file")
        os.remove(filename)

    except Exception as e:
        await msg.reply_text(f"❌ Error: {e}")


print("🤖 Bot started...")
app.run()
