from pyrogram import Client, Filters, Message
from os import getenv
import asyncio
from .configures import mongo

ADMIN = getenv("ADMIN")


@Client.on_message(Filters.user([int(ADMIN)]))
async def set_enemy(_: Client, m: Message):
    text = m.text
    replyed = m.reply_to_message
    replyed_id = replyed.from_user.id if replyed else None
    if text.startswith("!setenemy"):
        yaro = text.replace("!setenemy ", "") if len(
            text.replace("!setenemy ", "")) > 0 else None
        yaro = yaro.strip()

        if (not replyed and not yaro) or not yaro.isnumeric():
            await m.edit("‍**این دستور را باید روی یک فرد ریپلای کنید یا ایدی عددی ان را بعد از دستور وارد کنید**")
            yaro = None
            await asyncio.sleep(2)
            await m.delete()
            return
        elif replyed:
            yaro = replyed_id
        if yaro:
            yaro = int(yaro)
            mongo.USERS.update_one(
                {"uid": yaro}, {"$set": {"enemy": "yes"}},upsert=True)
            await m.edit(f"**کاربر** `{yaro}‍` **به لیست دشمنان اضافه شد**")

    else:
        await m.continue_propagation()


@Client.on_message(Filters.user([int(ADMIN)]))
async def del_enemy(_: Client, m: Message):
    text = m.text
    replyed = m.reply_to_message
    replyed_id = replyed.from_user.id if replyed else None
    if text.startswith("!delenemy"):
        yaro = text.replace("!delenemy ", "") if len(
            text.replace("!delenemy ", "")) > 0 else None
        yaro = yaro.strip()

        if (not replyed and not yaro) or not yaro.isnumeric():
            await m.edit("‍**این دستور را باید روی یک فرد ریپلای کنید یا ایدی عددی ان را بعد از دستور وارد کنید**")
            yaro = None
            await asyncio.sleep(2)
            await m.delete()
            return
        elif replyed:
            yaro = replyed_id
        if yaro:
            yaro = int(yaro)
            mongo.USERS.update_one(
                {"uid": yaro}, {"$set": {"enemy": "no"}}, upsert=True)
            await m.edit(f"**کاربر** `{yaro}‍` **از لیست دشمنان خارج شد**")
    else:
        await m.continue_propagation()
