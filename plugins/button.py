# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🗝 𝙏𝙐𝙏𝙊𝙍𝙄𝘼𝙇 🗝", callback_data="about"),
                InlineKeyboardButton(text="✖️ 𝙏𝙐𝙏𝙐𝙋 ✖️", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🔹 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 2 🔹", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🗝 𝙏𝙐𝙏𝙊𝙍𝙄𝘼𝙇 🗝", callback_data="about"),
                InlineKeyboardButton(text="✖️ 𝙏𝙐𝙏𝙐𝙋 ✖️", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🔹 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 1 🔹", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="🗝 𝙏𝙐𝙏𝙊𝙍𝙄𝘼𝙇 🗝", callback_data="about"),
                InlineKeyboardButton(text="✖️ 𝙏𝙐𝙏𝙐𝙋 ✖️", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🗝 𝙏𝙐𝙏𝙊𝙍𝙄𝘼𝙇 🗝", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="🔹 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 1 🔹", url=client.invitelink),
                InlineKeyboardButton(text="🔹 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 2 🔹", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="✖️ 𝙏𝙐𝙏𝙐𝙋 ✖️", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🔹 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 2 🔹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="📂 𝘼𝙈𝘽𝙄𝙇 𝙁𝙄𝙇𝙀 📂",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🔹 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 1 🔹", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="📂 𝘼𝙈𝘽𝙄𝙇 𝙁𝙄𝙇𝙀 📂",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🔹 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 1 🔹", url=client.invitelink),
                InlineKeyboardButton(text="🔹 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 2 🔹", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="📂 𝘼𝙈𝘽𝙄𝙇 𝙁𝙄𝙇𝙀 📂",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
