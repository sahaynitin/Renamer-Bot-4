from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client as kinu6, filters
from ..database.database import *
from ..tools.text import TEXT
from ..config import Config
import os
import logging
logger = logging.getLogger(__name__)

################## Saving Cption 📝 ##################

@kinu6.on_message(filters.command("caption") & filters.private & filters.incoming)
async def save_caption(c, m):
    if Config.BANNED_USERS:
        if m.from_user.id in Config.BANNED_USERS:
            return await m.reply_text(TEXT.BANNED_USER_TEXT, quote=True)

    if Config.BOT_PASSWORD:
        is_logged = (await get_data(m.from_user.id)).is_logged
        if not is_logged and not Config.AUTH_USERS:
            return await m.reply_text(TEXT.NOT_LOGGED_TEXT, quote=True)
    
    download_location = f"{Config.DOWNLOAD_LOCATION}/{m.from_user.id}"
    await update_cap(m.from_user.id, m.message_id)
    await m.download(file_name=download_location)

    await m.reply_text(
        text=TEXT.SAVED_CUSTOM_THUMBNAIL,
        quote=True
    )
       
      
     
   
 
@kinu6.on_message(filters.command("deletecaption") & filters.incoming & filters.private)
async def delete_caption(c, m):
    if Config.BANNED_USERS:
        if m.from_user.id in Config.BANNED_USERS:
            return await m.reply_text(TEXT.BANNED_USER_TEXT, quote=True)

    if Config.BOT_PASSWORD:
        is_logged = (await get_data(m.from_user.id)).is_logged
        if not is_logged and not Config.AUTH_USERS:
            return await m.reply_text(TEXT.NOT_LOGGED_TEXT, quote=True)

    download_location = f"{Config.DOWNLOAD_LOCATION}/{m.from_user.id}"
    caption = (await get_data(m.from_user.id)).caption_id

    if not caption:
        text = TEXT.NO_CUSTOM_THUMB_NAIL_FOUND
    else:
        await update_caption(m.from_user.id, None)
        text = TEXT.DELETED_CUSTOM_THUMBNAIL

    try:
        os.remove(download_location)
    except:
        pass

    await m.reply_text(
        text=text,
        quote=True
    )

    
   
 
@kinu6.on_message(filters.command("showcaption") & filters.incoming & filters.private)
async def show_caption(c, m):
    if Config.BANNED_USERS:
        if m.from_user.id in Config.BANNED_USERS:
            return await m.reply_text(TEXT.BANNED_USER_TEXT, quote=True)

    if Config.BOT_PASSWORD:
        is_logged = (await get_data(m.from_user.id)).is_logged
        if not is_logged and not Config.AUTH_USERS:
            return await m.reply_text(TEXT.NOT_LOGGED_TEXT, quote=True)

    caption = (await get_data(m.from_user.id)).caption_id

    if not caption :
        await m.reply_text(
            text=TEXT.NO_CUSTOM_THUMB_NAIL_FOUND,
            quote=True
        )
    else:
        download_location = f"{Config.DOWNLOAD_LOCATION}/{m.from_user.id}"

        if not os.path.exists(download_location):
            cap_tion = await c.get_messages(m.chat.id, caption)
            try:
                download_location = await cap_tion.download(file_name=download_location)
            except:
                await update_caption(m.from_user.id, None)
                return await m.reply_text(text=TEXT.NO_CUSTOM_THUMB_NAIL_FOUND, quote=True)

        await m.reply_text(
            text=download_location,
            parse_mode="markdown",
            quote=True
        )


################## THE END 🛑 ##################
