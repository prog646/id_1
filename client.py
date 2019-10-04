from typing import Any, Union, Coroutine

from telethon.tl.types import Chat, Channel, User, PeerUser

from settings import api_hash, api_id
from telethon import TelegramClient, events, sync
from telethon.tl.types import UpdateShortMessage, PeerUser


client = TelegramClient('session', api_id, api_hash)


@client.on(events.NewMessage(chats=('https://t.me/bank_kuni')))
async def forward_message(event):
    msg = event.message.to_dict()['message']
    await client.send_message('legalactBot', msg)

client.start()
client.run_until_disconnected()