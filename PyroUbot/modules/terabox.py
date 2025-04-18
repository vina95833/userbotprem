from pyrogram import Client, filters
import requests
from PyroUbot import *

__MODULE__ = "ᴛᴇʀᴀʙᴏx"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇʀᴀʙᴏx ⦫</b>
<blockquote><b>
⎆ Perintah :
ᚗ <code>{0}tera</code> Link
⊶ Mendownload video dari terabox.</b></blockquote>
"""

@PY.UBOT("tera")
async def terabox_handler(client, message):
    if len(message.command) < 2:
        await message.reply_text("Gunakan perintah dengan format: /terabox <url>")
        return
    
    url = message.command[1]
    api_url = f"https://api.botcahx.eu.org/api/download/terabox?url={url}&apikey=@moire_mor"
    response = requests.get(api_url)
    
    if response.status_code != 200:
        await message.reply_text("⛔ Gagal mengambil data dari Terabox API.")
        return
    
    data = response.json()
    if not data.get("status"):
        await message.reply_text("⛔ Terabox API mengembalikan respons gagal.")
        return
    
    result_text = "💠 **Daftar File Terabox:**\n\n"
    for item in data.get("ᚗ result", []):
        name = item.get("ᚗ name", "Tidak diketahui")
        created = item.get("ᚗ created", "Tidak diketahui")
        files = item.get("ᚗ files", [])
        
        result_text += f"💠 **{name}** (Dibuat: {created})\n"
        for file in files:
            filename = file.get("ᚗ filename", "Tidak diketahui")
            size = file.get("ᚗ size", "Tidak diketahui")
            url = file.get("ᚗ url", "Tidak tersedia")
            result_text += f"🎞️ {filename} ({size} bytes)\n🔗 [Download]({url})\n\n"
    
    await message.reply_text(result_text, disable_web_page_preview=True)
