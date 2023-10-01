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
        bar = "▁▄▂▇▄▅▄▅▃"
    elif 2 < vip < 4:
        bar = "▁▃▇▂▅▇▄▅▃"
    elif 4 <= vip < 6:
        bar = "▃▁▇▂▅▃▄▃▅"
    elif 6 <= vip < 8:
        bar = "▃▄▂▄▇▅▃▅▁"
    elif 8 <= vip < 10:
        bar = "▁▃▄▂▇▃▄▅▃"
    elif 10 <= vip < 12:
        bar = "▃▁▄▂▅▃▇▃▅"
    elif 12 <= vip < 14:
        bar = "▁▇▄▂▅▄▅▃▄"
    elif 14 <= vip < 16:
        bar = "▁▃▅▇▂▅▄▃▇"
    elif 16 <= vip < 18:
        bar = "▃▅▂▅▇▁▄▃▁"
    elif 18 < vip < 20:
        bar = "▇▅▂▅▃▄▃▁▃"
    elif 20 <= vip < 22:
        bar = "▃▇▂▅▁▅▄▃▁"
    elif 22 <= vip < 24:
        bar = "▅▄▇▂▅▂▄▇▁"
    elif 24 <= vip < 26:
        bar = "▃▅▂▅▃▇▄▅▃"
    elif 26 <= vip < 28:
        bar = "▁▄▂▇▄▅▄▅▃"
    elif 28 <= vip < 30:
        bar = "▁▃▇▂▅▇▄▅▃"
    elif 30 <= vip < 32:
        bar = "▃▁▇▂▅▃▄▃▅"
    elif 32 <= vip < 34:
        bar = "▃▄▂▄▇▅▃▅▁"
    elif 34 <= vip < 36:
        bar = "▁▃▄▂▇▃▄▅▃"
    elif 36 <= vip < 38:
        bar = "▃▁▄▂▅▃▇▃▅"
    elif 38 <= vip < 40:
        bar = "▁▇▄▂▅▄▅▃▄"
    elif 40 <= vip < 42:
        bar = "▁▃▅▇▂▅▄▃▇"
    elif 42 <= vip < 44:
        bar = "▃▅▂▅▇▁▄▃▁"
    elif 44 <= vip < 46:
        bar = "▇▅▂▅▃▄▃▁▃"
    elif 46 <= vip < 48:
        bar = "▃▇▂▅▁▅▄▃▁"
    elif 48 <= vip < 50:
        bar = "▅▄▇▂▅▂▄▇▁"
    elif 50 <= vip < 52:
        bar = "▃▅▂▅▃▇▄▅▃"
    elif 52 <= vip < 54:
        bar = "▁▄▂▇▄▅▄▅▃"
    elif 54 <= vip < 56:
        bar = "▁▃▇▂▅▇▄▅▃"
    elif 56 <= vip < 58:
        bar = "▃▁▇▂▅▃▄▃▅"
    elif 58 <= vip < 60:
        bar = "▃▄▂▄▇▅▃▅▁"
    elif 60 <= vip < 62:
        bar = "▁▃▄▂▇▃▄▅▃"
    elif 62 <= vip < 64:
        bar = "▃▁▄▂▅▃▇▃▅"
    elif 64 <= vip < 68:
        bar = "▁▇▄▂▅▄▅▃▄"
    elif 68 <= vip < 70:
        bar = "▁▃▅▇▂▅▄▃▇"
    elif 70 <= vip < 72:
        bar = "▃▅▂▅▇▁▄▃▁"
    elif 72 <= vip < 74:
        bar = "▇▅▂▅▃▄▃▁▃"
    elif 74 <= vip < 76:
        bar = "▃▇▂▅▁▅▄▃▁"
    elif 76 <= vip < 78:
        bar = "▅▄▇▂▅▂▄▇▁"
    elif 78 <= vip < 80:
        bar = "▃▅▂▅▃▇▄▅▃"
    elif 80 <= vip < 82:
        bar = "▁▄▂▇▄▅▄▅▃"
    elif 82 < vip < 84:
        bar = "▁▃▇▂▅▇▄▅▃"
    elif 84 <= vip < 86:
        bar = "▃▁▇▂▅▃▄▃▅"
    elif 88 <= vip < 90:
        bar = "▃▄▂▄▇▅▃▅▁"
    elif 90 <= vip < 92:
        bar = "▁▃▄▂▇▃▄▅▃"
    elif 92 <= vip < 94:
        bar = "▃▁▄▂▅▃▇▃▅"
    elif 94 <= vip < 96:
        bar = "▁▇▄▂▅▄▅▃▄"
    elif 96 <= vip < 98:
        bar = "▁▃▅▇▂▅▄▃▇"
    elif 98 <= vip < 100:
        bar = "▃▅▂▅▇▁▄▃▁"
    else:
        bar = "▇▅▂▅▃▄▃▁▃"

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
                text="𝙶𝚁𝙾𝚄𝙿", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙾𝚆𝙽𝙴𝚁", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙲𝙻𝙾𝚂𝙴", callback_data=f"close"
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
        bar = "▃▁▄▂▅▃▇▃▅"
    elif 10 < vip < 20:
        bar = "▁▇▄▂▅▄▅▃▄"
    elif 20 <= vip < 30:
        bar = "▁▃▅▇▂▅▄▃▇"
    elif 30 <= vip < 40:
        bar = "▃▅▂▅▇▁▄▃▁"
    elif 40 <= vip < 50:
        bar = "▇▅▂▅▃▄▃▁▃"
    elif 50 <= vip < 60:
        bar = "▁▄▂▇▄▅▄▅▃"
    elif 60 <= vip < 70:
        bar = "▁▃▇▂▅▇▄▅▃"
    elif 70 <= vip < 80:
        bar = "▃▁▇▂▅▃▄▃▅"
    elif 80 <= vip < 95:
        bar = "▃▄▂▄▇▅▃▅▁"
    else:
        bar = "▁▃▄▂▇▃▄▅▃"

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
                text="𝙶𝚁𝙾𝚄𝙿", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙾𝚆𝙽𝙴𝚁", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙲𝙻𝙾𝚂𝙴", callback_data=f"close"
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
                text="𝙶𝚁𝙾𝚄𝙿", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙾𝚆𝙽𝙴𝚁", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙲𝙻𝙾𝚂𝙴", callback_data=f"close"
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
                text="𝙶𝚁𝙾𝚄𝙿", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙾𝚆𝙽𝙴𝚁", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙲𝙻𝙾𝚂𝙴", callback_data=f"close"
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
                        text="𝙲𝙻𝙾𝚂𝙴", callback_data="close"
                    ),
                    InlineKeyboardButton(
                text="𝙾𝚆𝙽𝙴𝚁", url=f"https://t.me/itz_Lucky_Raja"
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
                text="𝙶𝚁𝙾𝚄𝙿", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=config.SUPPORT_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙾𝚆𝙽𝙴𝚁", url=f"https://t.me/itz_Lucky_Raja"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝙲𝙻𝙾𝚂𝙴", callback_data=f"close"
            )
        ],
    ]
    return buttons
