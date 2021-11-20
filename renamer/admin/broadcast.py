# USED PREVIOUS 

from pyrogram import filters

from renamer.config import Config
from pyrogram import Client as kinu6, filters


@kinu6.on_message(
    filters.private
    & filters.command("broadcast")
    & filters.user(Config.AUTH_USERS)
    & filters.reply
)
async def broadcast_(c, m):
    await c.start_broadcast(
        broadcast_message=m.reply_to_message, admin_id=m.from_user.id
    )
