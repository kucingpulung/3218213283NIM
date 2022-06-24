# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"𝙒𝙄𝘽𝙐 3𝙇𝙄𝙏𝙀 𝘽𝙊𝙏\n\n𝐓𝐮𝐭𝐨𝐫𝐢𝐚𝐥 :\n➥ 1. Start Bot,\n➥ 2. Join Channel 1 2,\n➥ 3. Klik 📂 𝘼𝙈𝘽𝙄𝙇 𝙁𝙄𝙇𝙀 📂,\n➥ 4. Tunggu hingga File nya Muncul.\n\n⚠️Jangan spam bot, tunggu beberapa detik sampai file muncul⚠️\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🏷 𝙍𝙀𝙋𝙊 🏷", url = f'https://t.me/wibu_3lite'),
                        InlineKeyboardButton("✖️ 𝙏𝙐𝙏𝙐𝙋 ✖️", callback_data="close"),
                    ],
                ]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
