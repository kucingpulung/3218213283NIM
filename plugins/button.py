from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="π πππππππΌπ π", callback_data="about"),
                InlineKeyboardButton(text="βοΈ πππππ βοΈ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="πΉ πΎππΌππππ 2 πΉ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="π πππππππΌπ π", callback_data="about"),
                InlineKeyboardButton(text="βοΈ πππππ βοΈ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="πΉ πΎππΌππππ 1 πΉ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="π πππππππΌπ π", callback_data="about"),
                InlineKeyboardButton(text="βοΈ πππππ βοΈ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="πΉ πΎππΌππππ 1 πΉ", url=client.invitelink),
                InlineKeyboardButton(text="πΉ πΎππΌππππ 2 πΉ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="π πππππππΌπ π", callback_data="about"),
            ],
            [InlineKeyboardButton(text="βοΈ πππππ βοΈ", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="πΉ πΎππΌππππ 2 πΉ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="π πΌππ½ππ ππππ π",
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
                InlineKeyboardButton(text="πΉ πΎππΌππππ 1 πΉ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="π πΌππ½ππ ππππ π",
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
                InlineKeyboardButton(text="πΉ πΎππΌππππ 1 πΉ", url=client.invitelink),
                InlineKeyboardButton(text="πΉ πΎππΌππππ 2 πΉ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="π πΌππ½ππ ππππ π",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
