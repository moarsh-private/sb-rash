from pyrogram import Client, Filters, Message
from os import getenv
from .configures import mongo
import asyncio




ADMIN = int(getenv("ADMIN"))
print(f"{ADMIN=}")


@Client.on_message(Filters.user([ADMIN])  & (Filters.group | Filters.channel))
async def mute(_: Client, m: Message):
    text = m.text
    replyed = m.reply_to_message
    replyed_id = replyed.from_user.id if replyed else None
    cid = m.chat.id 
    if text == "!mute":
        if not replyed:
            mongo.USERS.update_one({"cid": cid}, {
                "$set": {f"mute": "yes"}}, upsert=True)
            await m.edit(f"**Chat** `{cid}` **Muted**")
            await asyncio.sleep(2)
            await m.delete()
        else:
            mongo.USERS.update_one({"uid": replyed_id}, {
                "$set": {f"{cid}-mute": "yes"}}, upsert=True)
            await m.edit(f"**User** `{replyed_id}` **Muted in** `{cid}`")
            await asyncio.sleep(2)
            await m.delete()
    else:
        await m.continue_propagation()


@Client.on_message(Filters.user([ADMIN]) & (Filters.group | Filters.channel))
async def unmute(_: Client, m: Message):
    text = m.text
    replyed = m.reply_to_message
    replyed_id = replyed.from_user.id if replyed else None
    cid = m.chat.id 
    if text == "!unmute":
        if not replyed:
            mongo.USERS.update_one({"cid": cid}, {
                "$set": {f"mute": "no"}}, upsert=True)
            await m.edit(f"**Chat** `{cid}` **Unmuted**")
            await asyncio.sleep(2)
            await m.delete()
            
        else:
            mongo.USERS.update_one({"uid": replyed_id}, {
                "$set": {f"{cid}-mute": "no"}}, upsert=True)
            await m.edit(f"**User** `{replyed_id}` **Unmuted in** `{cid}`")
            await asyncio.sleep(2)
            await m.delete()
    else:
        await m.continue_propagation()
