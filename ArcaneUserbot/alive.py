import asyncio
from ArcaneUserbot.helpers.command import commandpro
from pyrogram import Client
from pyrogram.types import Message


@Client.on_message(commandpro(["!alive", "/alive", "/start", "!Arcane"]))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b7d01ce18bc5b66491a16.jpg",
        caption=f"""**ð· Êá´ÊÊá´, Éª á´á´ á´á´sÉªá´+á´ Éªá´á´á´ á´É´á´ sá´á´á´ á´sá´ÊÊá´á´ á´á´á´á´ ÊÊ @Arcane_bots ...ð¥ 
âââââââââââââââââââ
â£â á´á´á´á´á´á´s : [ÆÆ¦ÆÆÆÐ](https://t.me/ARcane_bots)
â£â sá´á´á´á´Êá´ : [ÆÆ¦ÆÆÆÐ](https://t.me/Arcane_X_Support)
â£â á´Êá´á´á´á´Ê : [á´¢á´á´s-xá´](https://t.me/II_ZEUS_XD_II)
â£â á´á´sá´ á´á´á´: [á´á´ á´á´á´Êá´Ê]()
âââââââââââââââââââ**""")


