#
# Copyright (C) 2022-2023 by StormBeatz@Github, < https://github.com/StormBeatz >.
#
# This file is part of < https://github.com/StormBeatz/StormBeatz > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/StormBeatz/StormBeatz/blob/master/LICENSE >
#
# All rights reserved.
#

from StormBeatz import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""**ʜɪ ɢᴜʏs, MENTION !!\n\nᴛʜɪs ɪs ᴅᴏʀᴀ ʀᴏʙᴏᴛ.\n\nᴛʜᴇ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.\n\nᴀʟʟ ᴏғ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴀʀᴇ ʟɪsᴛᴇᴅ ɪɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏ ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ʙʏ ᴛʏᴘᴇ /help.**
"""

COMMANDS_TEXT = f"""
✨ **ʜᴇʟʟᴏ MENTION !**
**ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url="https://t.me/fLyLoNg"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/NOOBXCREATOR"
            ),
            InlineKeyboardButton(
                text="sᴏᴘᴘᴏʀᴛ", url="https://t.me/NOOBCREATOR"
            ),                       
        ],        
        [
            InlineKeyboardButton(
                text="ɢɪғᴛ ʜᴇʀᴇ", url="https://t.me/pirokid"
            ),                                  
        ]
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(

                        "ᴀᴅᴅ ᴍᴇ ɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ",

                        url=f"https://t.me/DORAROBOT?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data="settings_back_helper")],

                







                [

                    InlineKeyboardButton(

                        "ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/NOOBXCREATOR"

                    ),

                    InlineKeyboardButton(

                        "sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/NOOBCREATOR"

                    ),

                ],
                [
                 InlineKeyboardButton("ʟᴀɴɢᴜᴀɢᴇ", callback_data="LG"
            ),
        ],
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", url="https://telegra.ph/StormBeatz-Music-Bot-Commands-11-07"
            ),            
            InlineKeyboardButton(
                text="Extra Commands", url="https://telegra.ph/StormBeatz-Music-Bot-Extra-Commands-11-07"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="Sudo Commands", url="https://telegra.ph/StormBeatz-Music-Bot-Sudo-Commands-11-07"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Extra Commands", url="https://telegra.ph/StormBeatz-Music-Bot-Extra-Commands-11-07"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Sudo Commands", url="https://telegra.ph/StormBeatz-Music-Bot-Sudo-Commands-11-07"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
✅ Admin Commands:

c stands for channel play.

/pause or /cpause - Pause the playing music.
/resume or /cresume- Resume the paused music.
/mute or /cmute- Mute the playing music.
/unmute or /cunmute- Unmute the muted music.
/skip or /cskip- Skip the current playing music.
/stop or /cstop- Stop the playing music.
/shuffle or /cshuffle- Randomly shuffles the queued playlist.
/seek or /cseek - Forward Seek the music to your duration
/seekback or /cseekback - Backward Seek the music to your duration
/restart - Restart bot for your chat .


✅ Specific Skip:
/skip or /cskip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

✅ Loop Play:
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.

✅ Auth Users:
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.
"""

AUTH_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

BOT_TEXT = """
✅--**Bot Commands:**--
/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.
/sudolist - Check Sudo Users of StormBeatz Music Bot
/lyrics [Music Name] - Searches Lyrics for the particular Music on web.
/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.
c stands for channel play.
/queue or /cqueue- Check Queue List of Music.
"""

PLAY_TEXT = """
✅--**Play Commands:**--
Available Commands = play , vplay , cplay
ForcePlay Commands = playforce , vplayforce , cplayforce
c stands for channel play.
v stands for video play.
force stands for force play.
/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.
/playforce or /vplayforce or /cplayforce -  Force Play stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.
/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.
✅--**Bot's Server Playlist:**--
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers.
"""


BASIC_TEXT = """
💠 **Basic Commands:**
/start - Start the bot
/help - Get help message
/play - Play songs or videos in vc
/vplay - Play video in VC
/settings - Check Settings of bot in your group
**Some Useful Commands :** 
/pause /resume /skip /end /loop /shuffle
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

ADMIN_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Auth Commands", callback_data="auth_cmds"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Help", callback_data="settings_back_helper"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                "Support", url=f"https://t.me/StormSupportChat"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)
