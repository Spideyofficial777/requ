import logging
import threading
import socket

from pyrogram import Client
from leave import register_leave_handler
from Script import script
from configs import API_ID, API_HASH, BOT_TOKEN


# Create a shared Pyrogram client instance
app = Client("approver_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


# Optional: TCP health check server for Koyeb
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


# Run the bot
if __name__ == "__main__":
    from commands import *  # Register all handlers
    register_leave_handler(app)

    logging.basicConfig(level=logging.INFO)
    print(script.LOGO_MSG)

    start_tcp_healthcheck_server(port=8080)
    app.run()