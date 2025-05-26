#rohit_1888

#rohit_1888

import os
import asyncio
from aiofiles import os
import time
import logging
import random
from pyrogram import Client, filters, enums
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    UserIsBlocked,
    UserNotParticipant,
    MessageTooLong,
    PeerIdInvalid,
)
from Spidey.database import get_all_users, add_user, already_db
from aiogram import Bot, Dispatcher, types
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Script import script
from leave import register_leave_handler
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pymongo.errors import PyMongoError
from configs import *
import threading
import socket
from pyrogram.enums import ChatMembersFilter



def start_tcp_healthcheck_server(port=8080):
    def server():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('0.0.0.0', port))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    conn.sendall(b"OK")

    thread = threading.Thread(target=server, daemon=True)
    thread.start()


# Initialize the bot
app = Client("approver_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)




if __name__ == "__main__":
    register_leave_handler(app)
    logging.basicConfig(level=logging.INFO)
    print(script.LOGO_MSG)

    start_tcp_healthcheck_server(port=8080)  # Starts TCP server on port 8080 for health checks
    app.run()
