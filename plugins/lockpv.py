from pyrogram import Client, Filters, Message
from os import getenv
from .configures import mongo


ADMIN = int(getenv("ADMIN"))
print(f"{ADMIN=}")


@Client.on_message(Filters.user([ADMIN]))
async def lock(_: Client, m: Message):
    text = m.text
    replyed = m.reply_to_message
    replyed_id = replyed.from_user.id if replyed else None
    if text == "!lockpv":
        if not replyed:
            mongo.ADMIN.update_one(
                {"uid": ADMIN}, {"$set": {"lockpv": "yes"}}, upsert=True)
            await m.edit("**Pv Locked**")
        else:
            mongo.USERS.update_one({"uid": replyed_id}, {
                "$set": {"locked": "yes"}}, upsert=True)
            await m.edit(f"**Pv For User** `{replyed_id}` **Locked**")
    else:
        await m.continue_propagation()


@Client.on_message(Filters.user([ADMIN]))
async def unlock(_: Client, m: Message):
    text = m.text
    replyed = m.reply_to_message
    replyed_id = replyed.from_user.id if replyed else None
    if text == "!unlockpv":
        if not replyed:
            mongo.ADMIN.update_one(
                {"uid": ADMIN}, {"$set": {"lockpv": "no"}}, upsert=True)
            await m.edit("**Pv Unlocked**")
        else:
            mongo.USERS.update_one({"uid": replyed_id}, {
                "$set": {"locked": "no"}}, upsert=True)
            await m.edit(f"**Pv For User** `{replyed_id}` **Unlocked**")
    else:
        await m.continue_propagation()
