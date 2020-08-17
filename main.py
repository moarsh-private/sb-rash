from pyrogram import Client,Filters
import logging

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

app = Client('rain',app_version="1.0.0",device_model="@beQrity Self Bot",system_version="v1.0",)

app.run()
