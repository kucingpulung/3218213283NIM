# (ยฉ)Codexbotz
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
            text=f"๐๐๐ฝ๐ 3๐๐๐๐ ๐ฝ๐๐\n\n๐๐ฎ๐ญ๐จ๐ซ๐ข๐๐ฅ :\nโฅ 1. Start Bot,\nโฅ 2. Join Channel 1 2,\nโฅ 3. Klik ๐ ๐ผ๐๐ฝ๐๐ ๐๐๐๐ ๐,\nโฅ 4. Tunggu hingga File nya Muncul.\n\nโ ๏ธJangan spam bot, tunggu beberapa detik sampai file munculโ ๏ธ\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("๐ท ๐๐๐๐ ๐ท", url = f'https://t.me/wibu_3lite'),
                        InlineKeyboardButton("โ๏ธ ๐๐๐๐๐ โ๏ธ", callback_data="close"),
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
