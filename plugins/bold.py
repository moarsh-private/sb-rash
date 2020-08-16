from pyrogram import Client, Filters, Message
from os import getenv
import asyncio
from .configures import mongo

ADMIN = int(getenv("ADMIN"))


@Client.on_message(Filters.user([ADMIN]))
async def bold_mode(_: Client, m: Message):
    text = m.text
    if text == "!boldmode on":
        mongo.ADMIN.update_one({"uid": ADMIN}, {
                               "$set": {"boldmode": "yes"}}, upsert=True)


        mongo.ADMIN.update_one({"uid": ADMIN}, {
                               "$set": {"monomode": "no"}}, upsert=True)
        await m.edit("**حالت bold فعال شد **")
    elif text == "!boldmode off":
        mongo.ADMIN.update_one({"uid": ADMIN}, {
                               "$set": {"boldmode": "no"}}, upsert=True)
        await m.edit("**حالت bold غیر فعال شد **")
    else:
        await m.continue_propagation()
