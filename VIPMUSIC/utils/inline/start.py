from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="🌱 Hᴇʟᴩ 🌱", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="🥹Sᴇᴛᴛɪɴɢꜱ🥹", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="🌹 𝐆ʀᴏᴜᴩ 🌹", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💀 Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴩ 💀",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🌱 Hᴇʟᴩ 🌱", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="❤️‍🔥Dᴇᴠᴇʟᴏᴩʀ ❤️‍🔥", url=f"https://t.me/Sxn0w"),
        ],
        [
            InlineKeyboardButton(text="🪴 𝐆ʀᴏᴜᴩ 🪴", url=config.SUPPORT_CHAT)
        ],
    ]
    return buttons
