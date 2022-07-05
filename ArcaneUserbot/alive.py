import asyncio
from ArcaneUserbot.helpers.command import commandpro
from pyrogram import Client
from pyrogram.types import Message


@Client.on_message(commandpro(["!alive", "/alive", "/start", "!Arcane"]))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b7d01ce18bc5b66491a16.jpg",
        caption=f"""**🍷 ʜᴇʟʟᴏ, ɪ ᴀᴍ ᴍᴜsɪᴄ+ᴠɪᴅᴇᴏ ᴀɴᴅ sᴘᴀᴍ ᴜsᴇʀʙᴏᴛ ᴍᴀᴅᴇ ʙʏ @Arcane_bots ...🥀 
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴜᴘᴅᴀᴛᴇs : [ƛƦƇƛƝЄ](https://t.me/ARcane_bots)
┣★ sᴜᴘᴘᴏʀᴛ : [ƛƦƇƛƝЄ](https://t.me/Arcane_X_Support)
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴢᴇᴜs-xᴅ](https://t.me/II_ZEUS_XD_II)
┣★ ᴊᴜsᴛ ᴛᴀᴘ: [ᴛᴏ ᴅᴇᴘʟᴏʏ]()
┗━━━━━━━━━━━━━━━━━┛**""")


