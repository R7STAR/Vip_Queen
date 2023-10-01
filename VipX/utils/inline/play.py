import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from VipX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
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
     elif 80 <= vip < 90: 
         bar = "————————✪ʟőⱱė✪—" 
     elif 90 <= vip < 100: 
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
    anon = math.floor(percentage)
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
    elif 80 <= vip < 90:
        bar = "————————✪ʟőⱱė✪—"
    elif 90 <= vip < 100:
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
