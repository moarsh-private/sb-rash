from pyrogram import Client, Filters, Message
from os import getenv
import asyncio
from .configures import mongo

ADMIN = int(getenv("ADMIN"))


@Client.on_message(Filters.user([ADMIN]))
async def slow_type(_: Client, m: Message):
    text = m.text
    if text.startswith("#s"):
        text = text.replace("#s", "").strip()
        char = ""
        for i in text:
            char += i
            if char.strip() in ("", " ") or i.strip() in ("", " "):
                continue
            await m.edit(char)
            await asyncio.sleep(0.3)
    elif text == "!slowmode on":
        mongo.ADMIN.update_one({"uid":ADMIN}, {
                               "$set": {"slowmode": "yes"}}, upsert=True)
        await m.edit("**حالت ارام فعال شد **")
    elif text == "!slowmode off":
        mongo.ADMIN.update_one({"uid":ADMIN}, {
                               "$set": {"slowmode": "no"}}, upsert=True)
        await m.edit("**حالت ارام غیر فعال شد **")
    else:
        await m.continue_propagation()
