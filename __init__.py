from pyrogram import Client,Filters
import settings
import os
print(os.getenv("NAME"))


app = Client("bot",app_version="1.0.0",device_model="@beQrity Self Bot",system_version="v1.0")

app.run()