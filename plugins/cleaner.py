from pyrogram import Client, Filters, Message
from os import getenv
import asyncio
from .configures import mongo

ADMIN = int(getenv("ADMIN"))


@Client.on_message(Filters.user([ADMIN]))
async def cleaner(_: Client, m: Message):
    text = m.text
    cid = m.chat.id 
    mid = int(m.message_id)
    replyed = m.reply_to_message
    if text.startswith("!clean"):
        await m.delete()
        num = text.replace("!clean","").strip()
        if len(num)>0 and not replyed:
            if not num.isnumeric():
                await m.edit("باید تعداد مسیج هارا یه صورت عدد وارد کنید")
                return
            num = int(num)
            rng = range(mid,mid-num,-1)
        elif replyed:
            num = int(num)
            rng = range(replyed.message_id,replyed.message_id-num,-1)
        else:
            rng = range(mid)
        print(rng)
        await _.delete_messages(cid,list(rng))    
        
    else:
        await m.continue_propagation()
