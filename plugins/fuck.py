from pyrogram import Client, Filters, Message
from os import getenv
from .configures import mongo
import asyncio

a = """
. 
                          /¯ )
                        /¯  /
                      /    /
              /´¯/'   '/´¯ )
           /'/   /     /    / / \
          ('(   (   (   (     |/    )
          \                       ./
           \                _.•´
             \              (
               \             \


"""

b = """
. 
                       
              /´¯/´¯/´¯ )
           /'/   /     /    / / \
          ('(   (   (   (     |/    )
          \                       ./
           \                _.•´
             \              (
               \             \
"""


ADMIN = int(getenv("ADMIN"))
print(f"{ADMIN=}")


@Client.on_message(Filters.user([ADMIN]))
async def fuck(_: Client, m: Message):
    text = m.text
    replyed = m.reply_to_message
    replyed_id = replyed.from_user.id if replyed else None
    cid = m.chat.id 
    if text == "!fuck":
        if not replyed:
            for i in range(10):
                await m.edit(a)
                await asyncio.sleep(0.3)
                await m.edit(b)
            await asyncio.sleep(2)
            await m.delete()
        else:
            await m.delete()
            x = await m.reply(reply_to_message_id=replyed.message_id)
            for i in range(10):
                await x.edit(a)
                await asyncio.sleep(0.3)
                await x.edit(b)
            await asyncio.sleep(2)
            await x.delete()
    else:
        await m.continue_propagation()

