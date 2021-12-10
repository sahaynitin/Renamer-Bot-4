import os
import traceback
import logging

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.emoji import *
from pyrogram import Client as kinu6, filters
from ..tools.text import TEXT
from ..config import Config
import logging
logger = logging.getLogger(__name__)

@kinu6.on_message(pyrogram.filters.command(["caption"]))
async def set_caption(bot, update):
    if len(update.command) == 1:
        await update.reply_text(
            "Custom Caption \n\n you can use this command to set your own caption  \n\n Usage : /scaption Your caption text \n\n note : For current file name use : <code>{filename}</code>", 
            quote = True, 
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Show Current Caption', callback_data = "view_caption")      
                ],
                [
                    InlineKeyboardButton('Delete Caption', callback_data = "del_caption")
                ]
            ]
        ) 
        )
    else:
        command, CSTM_FIL_CPTN = update.text.split(' ', 1)
        await update_cap(update.from_user.id, CSTM_FIL_CPTN)
        await update.reply_text(f"**--Your Caption--:**\n\n{CSTM_FIL_CPTN}", quote=True)

        
@kinu6.on_callback_query()
async def cb_handler(client: kinu6 , query: CallbackQuery):
    data = query.data
    
    if data == "caption":
        await query.message.edit_text(
            text=TEXT.CAPTION_TEXT,
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Show Current Caption', callback_data = "view_caption"),
                    InlineKeyboardButton("Delete Caption", callback_data = "del_caption")
                ],
                [
                    InlineKeyboardButton('Back', callback_data = "help"),
                    InlineKeyboardButton('🔒 Close', callback_data = "close_data")
                ]
            ]
        )
     )
     elif data =="view_caption":
        try:
            caption = await get_caption(query.from_user.id)
            c_text = caption.caption
           
        except:
            c_text = "Sorry but you haven't added any caption yet please set your caption through /caption command" 
           
        await query.message.edit(
            text=f"<b>Your Custom Caption:</b> \n\n{c_text} ",
            parse_mode="html",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('Back', callback_data = "caption"),
                        InlineKeyboardButton("🔒 Close", callback_data = "close_data")
                    ]
                ]
            )
        )
    
     elif data == "del_caption":
        try:
           await del_caption(query.from_user.id)   
        except:
            pass
        await query.message.edit_text(
            text="<b>caption deleted successfully</b>",
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Back', callback_data = "caption"),
                    InlineKeyboardButton("🔒 Close", callback_data = "close_data")
                ]
            ]
        )
     )
        
     elif data == "close_data":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
