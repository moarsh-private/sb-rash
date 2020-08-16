from pyrogram import Client, Filters, Message
from os import getenv
from .configures import mongo
import asyncio

ADMIN = getenv("ADMIN")

@Client.on_message(Filters.private)
async def pre_proccessing_pv(_: Client, m: Message):
    text = m.text
    uid = m.from_user.id
    user = mongo.USERS.find_one({"uid":uid})
    all_lock = mongo.ADMIN.find_one({"lockpv":"yes"})
    
    if all_lock:
        await m.delete()
    else:
        locked = user.get("locked")
        if locked == "yes":
            await m.delete()
        await m.continue_propagation()


@Client.on_message(Filters.user([int(ADMIN)]))
async def pre_proccessing_admin(_: Client, m: Message):
    text = m.text
    uid = m.from_user.id
    slow_mode = mongo.ADMIN.find_one({"slowmode":"yes"})
    mono_mode = mongo.ADMIN.find_one({"monomode":"yes"})
    bold_mode = mongo.ADMIN.find_one({"boldmode":"yes"})
    print(f"{mono_mode=}")
    print(f"{bold_mode=}")
    st = ""
    if mono_mode:
        await m.edit(f"`{text}`")
        st = "`"
    if bold_mode:
        await m.edit(f"**{text}**")
        st = "**"
    if slow_mode and text != "!slowmode off":
        char = ""
        for i in text:
            char += i
            if char.strip() in ("", " ") or i.strip() in (""," "):
                continue
            await m.edit(f"{st}{char}{st}")
            await asyncio.sleep(0.3)
    else:
        await m.continue_propagation()
    
