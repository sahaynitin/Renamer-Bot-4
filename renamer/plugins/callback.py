from pyrogram.emoji import *
from pyrogram.errors import UserBannedInChannel, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client as kinu6, filters
from ..tools.text import TEXT
from ..config import Config
from .commands import *
import logging
logger = logging.getLogger(__name__)


################## Callback for help button ##################

@kinu6.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()
    await help(c, m, True)


################## Callback for donate button ##################

@kinu6.on_callback_query(filters.regex('^donate$'))
async def donate(c, m):
    button = [[
        InlineKeyboardButton(
            f'{HOUSE_WITH_GARDEN} Home', callback_data='back'),
        InlineKeyboardButton(f'{ROBOT} About', callback_data='about')
    ], [
        InlineKeyboardButton(f'{NO_ENTRY} Close', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    await m.answer()
    await m.message.edit(
        text=TEXT.DONATE_USER.format(m.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


################## Callback for close button ##################

@kinu6.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


################## Callback for home button ##################

@kinu6.on_callback_query(filters.regex('^back$'))
async def back_cb(c, m):
    await m.answer()
    await start(c, m, True)


################## Callback for about button ##################

@kinu6.on_callback_query(filters.regex('^about$'))
async def about_cb(c, m):
    await m.answer()
    await about(c, m, True)
