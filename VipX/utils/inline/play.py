import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from VipX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    vip = math.floor(percentage)
    if 0 < vip <= 2:
        bar = "⚡𝙹𝙰𝙸ㅤ𝚂𝙷𝚁𝙴𝙴ㅤ𝚁𝙰𝙼⚡"
    elif 2 < vip < 4:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 4 <= vip < 6:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 6 <= vip < 8:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 8 <= vip < 10:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 10 <= vip < 12:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 12 <= vip < 14:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 14 <= vip < 16:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 16 <= vip < 18:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 18 < vip < 20:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 20 <= vip < 22:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 22 <= vip < 24:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 24 <= vip < 26:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 26 <= vip < 28:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 28 <= vip < 30:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 30 <= vip < 32:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 32 <= vip < 34:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 34 <= vip < 36:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 36 <= vip < 38:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 38 <= vip < 40:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 40 <= vip < 42:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 42 <= vip < 44:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 44 <= vip < 46:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 46 <= vip < 48:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 48 <= vip < 50:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 50 <= vip < 52:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 52 <= vip < 54:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 54 <= vip < 56:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 56 <= vip < 58:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 58 <= vip < 60:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 60 <= vip < 62:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 62 <= vip < 64:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 64 <= vip < 68:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 68 <= vip < 70:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 70 <= vip < 72:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 72 <= vip < 74:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 74 <= vip < 76:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 76 <= vip < 78:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 78 <= vip < 80:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 80 <= vip < 82:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 82 < vip < 84:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 84 <= vip < 86:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 88 <= vip < 90:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    elif 90 <= vip < 92:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 92 <= vip < 94:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙹𝙰ㅤㅤㅤㅤ"
    elif 94 <= vip < 96:
        bar = "ㅤㅤㅤㅤㅤ𝚁𝙰𝙼ㅤㅤㅤㅤㅤ"
    elif 96 <= vip < 98:
        bar = "ㅤㅤㅤㅤㅤ𝙹𝙰𝙸ㅤㅤㅤㅤ"
    elif 98 <= vip < 100:
        bar = "ㅤㅤㅤㅤㅤ𝚂𝙷𝚁𝙴𝙴ㅤㅤㅤ"
    else:
        bar = "𝙹𝙰𝙸 𝚂𝙸𝚈𝙰 𝚁𝙰𝙼"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥺", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="🍃", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🌦", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝚂𝙸𝚈𝙰", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝚁𝙰𝙼", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸ㅤ𝚂𝙸𝚈𝙰ㅤ𝚁𝙰𝙼", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    vip = math.floor(percentage)
    if 0 < vip <= 10:
        bar = "✪ʟőⱱė✪—————————"
    elif 10 < vip < 20:
        bar = "—✪ʟőⱱė✪————————"
    elif 20 <= vip < 30:
        bar = "——✪ʟőⱱė✪———————"
    elif 30 <= vip < 40:
        bar = "———✪ʟőⱱė✪——————"
    elif 40 <= vip < 50:
        bar = "————✪ʟőⱱė✪—————"
    elif 50 <= vip < 60:
        bar = "—————✪ʟőⱱė✪————"
    elif 60 <= vip < 70:
        bar = "——————✪ʟőⱱė✪———"
    elif 70 <= vip < 80:
        bar = "———————✪ʟőⱱė✪——"
    elif 80 <= vip < 95:
        bar = "————————✪ʟőⱱė✪—"
    else:
        bar = "—————————✪ʟőⱱė✪"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥺", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🌦", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝚂𝙸𝚈𝙰", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝚁𝙰𝙼", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸ㅤ𝚂𝙸𝚈𝙰ㅤ𝚁𝙰𝙼", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥺", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="🍃", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🌦", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝚂𝙸𝚈𝙰", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝚁𝙰𝙼", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸ㅤ𝚂𝙸𝚈𝙰ㅤ𝚁𝙰𝙼", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥺", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🌦", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝚂𝙸𝚈𝙰", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝚁𝙰𝙼", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸ㅤ𝚂𝙸𝚈𝙰ㅤ𝚁𝙰𝙼", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"VipPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"VipPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🦋",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🥺",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏꜱᴇ", callback_data="close"
                    ),
                    InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/itz_Lucky_Raja"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="🥺", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="❤️", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="🍃", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="🌦", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝚂𝙸𝚈𝙰", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝚁𝙰𝙼", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙹𝙰𝙸ㅤ𝚂𝙸𝚈𝙰ㅤ𝚁𝙰𝙼", callback_data=f"close"
            )
        ],
    ]
    return buttons
