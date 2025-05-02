from typing import List, Union
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import config
import logging

logger = logging.getLogger(__name__)

class ButtonManager:
    def __init__(self):
        self.force_sub_channel = config.FORCE_SUB_CHANNEL
        self.force_sub_channel_2 = config.FORCE_SUB_CHANNEL_2
        self.db_channel = config.DB_CHANNEL_ID

    async def check_force_sub(self, client, user_id: int) -> bool:
        try:
            if self.force_sub_channel != 0:
                member = await client.get_chat_member(self.force_sub_channel, user_id)
                if member.status in ["left", "kicked"]:
                    return False
            
            if self.force_sub_channel_2 != 0:
                member = await client.get_chat_member(self.force_sub_channel_2, user_id)
                if member.status in ["left", "kicked"]:
                    return False
                    
            return True
        except Exception as e:
            logger.error(f"Force sub check error: {str(e)}")
            return False

    async def show_start(self, client, callback_query: CallbackQuery):
        try:
            await callback_query.message.edit_text(
                config.Messages.START_TEXT.format(
                    bot_name=config.BOT_NAME,
                    user_mention=callback_query.from_user.mention
                ),
                reply_markup=self.start_button()
            )
        except Exception as e:
            logger.error(f"Show start error: {str(e)}")

    async def show_help(self, client, callback_query: CallbackQuery):
        try:
            await callback_query.message.edit_text(
                config.Messages.HELP_TEXT,
                reply_markup=self.help_button()
            )
        except Exception as e:
            logger.error(f"Show help error: {str(e)}")

    async def show_about(self, client, callback_query: CallbackQuery):
        try:
            await callback_query.message.edit_text(
                config.Messages.ABOUT_TEXT.format(
                    bot_name=config.BOT_NAME,
                    version=config.BOT_VERSION
                ),
                reply_markup=self.about_button()
            )
        except Exception as e:
            logger.error(f"Show about error: {str(e)}")

    def force_sub_button(self) -> InlineKeyboardMarkup:
        buttons = []
        
        if config.FORCE_SUB_CHANNEL != 0 and config.CHANNEL_LINK:
            buttons.append([
                InlineKeyboardButton(
                    "Join Channel 1 🔔",
                    url=config.CHANNEL_LINK
                )
            ])
            
        if config.FORCE_SUB_CHANNEL_2 != 0 and config.CHANNEL_LINK_2:
            buttons.append([
                InlineKeyboardButton(
                    "Join Channel 2 🔔",
                    url=config.CHANNEL_LINK_2
                )
            ])
            
        return InlineKeyboardMarkup(buttons)

    def start_button(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton("⚡️ ᴍᴀɪɴ ʜᴜʙ", url="t.me/seishiro_atanime"),
                InlineKeyboardButton("🍁 ʀᴀɴᴅᴏᴍ", url="t.me/seishiro_anime_is")
            ],
            [
                InlineKeyboardButton("🛈 ᴀʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("✘ ᴄʟᴏsᴇ", callback_data="close")
            ]
        ]
        return InlineKeyboardMarkup(buttons)
    
    def help_button(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton("⚡️ ᴍᴀɪɴ ʜᴜʙ", url="t.me/seishiro_atanime"),
                InlineKeyboardButton("🍁 ʀᴀɴᴅᴏᴍ", url="t.me/seishiro_anime_is")
            ],
            [
                InlineKeyboardButton("🛈 ᴀʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("✘ ᴄʟᴏsᴇ", callback_data="close")
            ]
        ]
        return InlineKeyboardMarkup(buttons)
    
    def about_button(self) -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data="close"),
                InlineKeyboardButton('🍁 ʙᴀᴄᴋ', callback_data="back")
            ]
        ]
        return InlineKeyboardMarkup(buttons)

    def file_button(self, file_uuid: str) -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton("Download 📥", callback_data=f"download_{file_uuid}"),
                InlineKeyboardButton("Share Link 🔗", callback_data=f"share_{file_uuid}")
            ]
        ]
        
        if config.CHANNEL_LINK:
            if config.CHANNEL_LINK_2:
                buttons.append([
                    InlineKeyboardButton("Channel 1 📢", url=config.CHANNEL_LINK),
                    InlineKeyboardButton("Channel 2 📢", url=config.CHANNEL_LINK_2)
                ])
            else:
                buttons.append([
                    InlineKeyboardButton("Channel 📢", url=config.CHANNEL_LINK)
                ])
        
        return InlineKeyboardMarkup(buttons)

    def batch_button(self, batch_uuid: str) -> InlineKeyboardMarkup:
        buttons = [
            [
                InlineKeyboardButton("Download All 📥", callback_data=f"dlbatch_{batch_uuid}"),
                InlineKeyboardButton("Share Link 🔗", callback_data=f"share_batch_{batch_uuid}")
            ]
        ]
        
        if config.CHANNEL_LINK:
            if config.CHANNEL_LINK_2:
                buttons.append([
                    InlineKeyboardButton("Channel 1 📢", url=config.CHANNEL_LINK),
                    InlineKeyboardButton("Channel 2 📢", url=config.CHANNEL_LINK_2)
                ])
            else:
                buttons.append([
                    InlineKeyboardButton("Channel 📢", url=config.CHANNEL_LINK)
                ])
        
        return InlineKeyboardMarkup(buttons)
