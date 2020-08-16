from pyrogram import Client, Filters, Message
from os import getenv
import asyncio
from .configures import mongo

ADMIN = int(getenv("ADMIN"))


@Client.on_message(Filters.user([ADMIN]))
async def mono_mode(_: Client, m: Message):
    text = m.text
    if text == "!monomode on":
        mongo.ADMIN.update_one({"uid": ADMIN}, {
                               "$set": {"monomode": "yes"}}, upsert=True)
        await m.edit("**حالت `mono` فعال شد **")
        mongo.ADMIN.update_one({"uid": ADMIN}, {
                               "$set": {"boldmode": "no"}}, upsert=True)
    elif text == "!monomode off":
        mongo.ADMIN.update_one({"uid": ADMIN}, {
                               "$set": {"monomode": "no"}}, upsert=True)
        
        await m.edit("**حالت `mono` غیر فعال شد **")
    else:
        await m.continue_propagation()
