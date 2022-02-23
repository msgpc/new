import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

bot = Client(
    "Remove FwdTag",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TXT = """
Hi {}, I'm Forward Tag Remover bot.\n\nForward me some messages, i will remove forward tag from them.\nAlso can do it in channels.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('PM Bots', url='https://t.me/PM_Bots'),
        ]]
    )


@bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@bot.on_message(filters.channel & filters.forwarded)
async def fwdrmv(c, m):
    if m.caption:                        
             caption = f"**{m.caption}**" 
    else:
             None
    if('t.me' in caption):
        caption = caption.replace('t.me',"@Pulikesi_Meme")
    else:
        caption = caption.replace("@Pulikesi_Meme - ","")
        caption = caption.replace(".mkv","")
        caption = caption.replace("HEVC","#HEVC")
        caption = caption + "\n\n**📥 JOIN : @Pulikesi_Meme**"    
    try:
        if m.media and not m.sticker:
            await m.copy(m.chat.id, caption)
            await m.delete()
        else:
            await m.copy(m.chat.id)
            await m.delete()
    except FloodWait as e:
        await asyncio.sleep(e.x)


@bot.on_message(filters.private | filters.group)
async def fwdrm(c, m):
    if m.caption:                        
             caption = f"**{m.caption}**" 
    else:
             None         
    caption = caption.replace("@Pulikesi_Meme - ","")
    caption = caption.replace(".mkv","")
    caption = caption.replace("HEVC","#HEVC")
    caption = caption + "\n\n**📥 JOIN : @Pulikesi_Meme**"
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
        else:
            await m.copy(m.chat.id)
    except FloodWait as e:
        await asyncio.sleep(e.x)


bot.run()
