import asyncio
from json import loads
from pyrogram import Client
from google_currency import convert
from settings import api_id, api_hash, amount


async def main():
    async with Client("pijawca", api_id=api_id, api_hash=api_hash) as app:
        json_object = loads(convert('rub', 'usd', int(amount)))
        await app.update_profile(last_name='[' + json_object['amount'] + ']')
        print('Profile updated as: [' + json_object['amount'] + ']')

asyncio.run(main())
