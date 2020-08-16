from pyrogram import Client, Filters,Message
from os import getenv
from selfbot.configures import mongo


ADMIN = getenv("ADMIN")

@Client.on_message(Filters.user(ADMIN))
async def lock(_:Client,m:Message):
    text = m.text
    print(text)
    cid = m.chat.id 
    replyed = m.reply_to_message
    replyed_id = replyed.from_user.id
    if text == "!lockpv":
        if not replyed:
            mongo.ADMIN.insert_one({"lockpv":"yes"})
            await m.edit("**Pv Locked**")
        else:
            user = mongo.USERS.find_one({"uid":replyed_id})
            if user:
                mongo.USERS.update_one({"uid":replyed_id},{"locked":"yes"})
            else:
                mongo.USERS.insert_one({"uid":replyed_id,"locked":"yes"})


