from pyrogram import Client, Filters, Message
from os import getenv
from .configures import mongo
import asyncio

ADMIN = getenv("ADMIN")

@Client.on_message(Filters.private)
async def pre_proccessing_pv(_: Client, m: Message):
    text = m.text
    uid = m.from_user.id
    user = mongo.USERS.find_one({"uid":uid}) or {}
    all_lock = mongo.ADMIN.find_one({"lockpv":"yes"})    
    if all_lock:
        await m.delete()
    else:
        locked = user.get("locked")
        if locked == "yes":
            await m.delete()
        await m.continue_propagation()

@Client.on_message(Filters.group | Filters.channel)
async def pre_proccessing_group_and_channel(_: Client, m: Message):    
    uid = m.from_user.id if m.from_user else 123456
    cid = m.chat.id
    mute = mongo.USERS.find_one({'uid':uid,f"{cid}-mute":'yes'})    
    muteall = mongo.USERS.find_one({f"cid":cid,'mute':'yes'})    
    if (mute or muteall) and uid != ADMIN:
        try:
            await m.delete()
        except: pass
    await m.continue_propagation()


@Client.on_message(Filters.user([int(ADMIN)]))
async def pre_proccessing_admin(_: Client, m: Message):
    text = m.text
    slow_mode = mongo.ADMIN.find_one({"slowmode":"yes"})
    mono_mode = mongo.ADMIN.find_one({"monomode":"yes"})
    bold_mode = mongo.ADMIN.find_one({"boldmode":"yes"})
    print(f"{mono_mode=}")
    print(f"{bold_mode=}")
    st = ""

    if slow_mode and text != "!slowmode off":
        char = ""
        for i in text:
            char += i
            if char.strip() in ("", " ") or i.strip() in (""," "):
                continue
            await m.edit(f"{st}{char}{st}")
            await asyncio.sleep(0.2)
    if mono_mode:
        await m.edit(f"`{text}`")
        st = "`"
    if bold_mode:
        await m.edit(f"**{text}**")
        st = "**"
    await m.continue_propagation()


