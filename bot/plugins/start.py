from pyrogram import filters as Filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..translations import Messages as tr
from ..config import Config
from ..utubebot import UtubeBot


@UtubeBot.on_message(
    Filters.private 
    & Filters.incoming
    & Filters.command('start')
    & Filters.user(Config.AUTH_USERS)
)
async def _start(c, m):
    await m.reply_chat_action("typing")
    
    await m.reply_text(
        text=tr.START_MSG.format(m.from_user.first_name),
        quote=True,
       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="⭕️ CHANNEL ⭕️", url="https://t.me/All_Movie_Rockers")], [InlineKeyboardButton(text="😇 SUPPORT", url="https://t.me/allmovierockerssdiscussion"),
                                                    InlineKeyboardButton(text="Creator ♐️", url="https://t.me/shreevish")]]),
        
        reply_to_message_id=update.message_id
    )
