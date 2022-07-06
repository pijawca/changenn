import asyncio
from requests import get
from json import loads
from pyrogram import Client
from google_currency import convert

api_id = #
api_hash = "#"

async def main():
    async with Client("free", api_id=api_id, api_hash=api_hash) as app:
        money = get('#')
        json_object = loads(convert('rub', 'usd', int(money)))
        await app.update_profile(last_name='[' + json_object['amount'] + ']')

asyncio.run(main())
