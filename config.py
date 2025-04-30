from typing import List, Dict
import os
from dotenv import load_dotenv


load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Database Configuration
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Channel Configuration 
DB_CHANNEL_ID = int(os.getenv("DB_CHANNEL_ID"))
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL")) # First force sub channel
FORCE_SUB_CHANNEL_2 = int(os.getenv("FORCE_SUB_CHANNEL_2", 0)) # Second force sub channel, defaults to 0 if not set

# Add a second channel link
CHANNEL_LINK = os.getenv("CHANNEL_LINK") # First channel link
CHANNEL_LINK_2 = os.getenv("CHANNEL_LINK_2", "") # Second channel link

# Bot Information
BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_NAME = os.getenv("BOT_NAME")
BOT_VERSION = "1.6"

# Privacy Mode Configuration and codexbotz delete time
PRIVACY_MODE = os.getenv("PRIVACY_MODE", "off").lower() == "on"
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 30))

# Your Modiji Url Api Key Here
MODIJI_API_KEY = os.getenv("MODIJI_API_KEY")
if not MODIJI_API_KEY:
    print("⚠️ Warning: MODIJI_API_KEY not set in environment variables")

# Links
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
DEVELOPER_LINK = os.getenv("DEVELOPER_LINK")
SUPPORT_LINK = os.getenv("SUPPORT_LINK")

# For Koyeb/render 
WEB_SERVER = bool(os.getenv("WEB_SERVER", True)) # make it True if deploying on koyeb/render else False
PING_URL = os.getenv("PING_URL") # add your koyeb/render's public url
PING_TIME = int(os.getenv("PING_TIME")) # Add time_out in seconds

# Admin IDs - Convert space-separated string to list of integers
ADMIN_IDS: List[int] = [
    int(admin_id.strip())
    for admin_id in os.getenv("ADMIN_IDS", "").split()
    if admin_id.strip().isdigit()
]

# File size limit (2GB in bytes)
MAX_FILE_SIZE = 2000 * 1024 * 1024

# Supported file types and extensions
SUPPORTED_TYPES = [
    "document",
    "video",
    "audio",
    "photo",
    "voice",
    "video_note",
    "animation"
]

SUPPORTED_EXTENSIONS = [
    # Documents
    "pdf", "txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
    # Programming Files
    "py", "js", "html", "css", "json", "xml", "yaml", "yml",
    # Archives
    "zip", "rar", "7z", "tar", "gz", "bz2",
    # Media Files
    "mp4", "mp3", "m4a", "wav", "avi", "mkv", "flv", "mov",
    "webm", "3gp", "m4v", "ogg", "opus",
    # Images
    "jpg", "jpeg", "png", "gif", "webp", "bmp", "ico",
    # Applications
    "apk", "exe", "msi", "deb", "rpm",
    # Other
    "txt", "text", "log", "csv", "md", "srt", "sub"
]

SUPPORTED_MIME_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/zip",
    "application/x-rar-compressed",
    "application/x-7z-compressed",
    "video/mp4",
    "audio/mpeg",
    "audio/mp4",
    "image/jpeg",
    "image/png",
    "image/gif",
    "application/vnd.android.package-archive",
    "application/x-executable",
]

class Messages:
    START_TEXT = """

ʙᴀᴋᴋᴀᴀᴀ!!! {user_mention}/n  ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.


Use /help to see available commands!/n
"""

    HELP_TEXT = """
📚 **Available Commands**  

👤 **User Commands:**  
• `/start` - Start the bot  
• `/help` - Show this menu  
• `/about` - Bot details  
• `/short [url]` - Shorten a link (e.g., `/short example.com`)  
/repo 

👑 **Admin Commands:**  
• `/upload` - Upload a file (reply to a file)  
• `/stats` - View bot statistics  
• `/broadcast` - Send a message to all users  
• `/auto_del` - Set auto-delete timer  


🗑 **Auto-Delete System:**  
• Files auto-delete after a set time.  
• Modify timer using `/auto_del`.  

🔗 **Batch System:**  
• `/batch` - Group multiple files into one link.  
• Forward files & reply with `/batch`.  


"""

    ABOUT_TEXT = """

<b>○ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/rohitreddy4'>Rohit</a>\n"
    "○ Developer: <a href='https://t.me/adityaabhinav'>Aditya Abhinav</a>\n"
    "○ Lɪʙʀᴀʀʏ: <a href='https://github.com/pyrogram/pyrogram'>Pʏʀᴏɢʀᴀᴍ</a>\n"
    "○ Mᴀɪɴ Cʜᴀɴɴᴇʟ: <a href='https://t.me/seishiro_atanime'>Seishiro At Anime</a>\n"
    "○ Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ: <a href='https://t.me/seishiro_anime_is'>Seishiro Anime </a></b>"

"""

    FILE_TEXT = """
📁 **File Details**

**Name:** `{file_name}`
**Size:** {file_size}
**Type:** {file_type}
**Downloads:** {downloads}
**Uploaded:** {upload_time}
**By:** {uploader}

🔗 **Share Link:**
`{share_link}`
"""

    FORCE_SUB_TEXT = """
⚠️ **Access Restricted!**

Please join our channel to use this bot:

Click button below, then try again!
"""

class Buttons:
    def start_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                InlineKeyboardButton("⚡️ ᴍᴀɪɴ ʜᴜʙ", url = "t.me/seishiro_atanime"),
                InlineKeyboardButton("🍁 ʀᴀɴᴅᴏᴍ", url = "t.me/seishiro_anime_is")
            ],
                [
                    InlineKeyboardButton("🛈 ᴀʙᴏᴜᴛ", callback_data = "about"),
                    InlineKeyboardButton("✘ ᴄʟᴏsᴇ", callback_data = "close")
                    ]
        ]

    
    def about_buttons() -> List[List[Dict[str, str]]]:
        return [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ʙᴀᴄᴋ', callback_data = "back")
                    ]
                ]

    def file_buttons(file_uuid: str) -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Download 📥", "callback_data": f"download_{file_uuid}"},
                {"text": "Share 🔗", "callback_data": f"share_{file_uuid}"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]


class Progress:
    PROGRESS_BAR = "█"
    EMPTY_PROGRESS_BAR = "░"
    PROGRESS_TEXT = """
**{0}** {1}% 

**⚡️ Speed:** {2}/s
**💫 Done:** {3}
**💭 Total:** {4}
**⏰ Time Left:** {5}
"""
  
