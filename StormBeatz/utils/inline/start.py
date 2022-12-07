#
# Copyright (C) 2021-2022 by StormBeatz@Github, < https://github.com/StormBeatz >.
#
# This file is part of < https://github.com/StormBeatz/StormBeatz > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/StormBeatz/StormBeatz/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="ʙᴏᴛ ᴏᴡɴᴇʀ", url="https://t.me/flylong"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/noobxcreator"
            ),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/noobcreator"
            ),                       
        ],        
        [
            InlineKeyboardButton(
                text="ɢɪғᴛ ʜᴇʀᴇ", url="https://t.me/pirokid"
            ),                                  
        ]
    ]
    return buttons


def private_panel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/noobxcreator"),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/noobcreator"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="ʟᴀɴɢᴜᴀɢᴇ", callback_data="LG"
                )
        ],
        [
            InlineKeyboardButton(
                text="ɢɪғᴛ ʜᴇʀᴇ", url="https://t.me/pirokid"
            )
        ]
     ]
    return buttons
