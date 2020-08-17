from pyrogram import Client, Filters, Message
from os import getenv
from .configures import mongo


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
            await m.edit("باید روی یک نفر ریپلای کنید")
        else:
            mongo.USERS.update_one({"uid": replyed_id}, {
                "$set": {f"{cid}-mute": "yes"}}, upsert=True)
            await m.edit(f"**User** `{replyed_id}` **Muted in** `{cid}")
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
            await m.edit("باید روی یک نفر ریپلای کنید")
        else:
            mongo.USERS.update_one({"uid": replyed_id}, {
                "$set": {f"{cid}-mute": "no"}}, upsert=True)
            await m.edit(f"**User** `{replyed_id}` **Unmuted in** `{cid}")
    else:
        await m.continue_propagation()
