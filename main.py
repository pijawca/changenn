import asyncio
from requests import get
from json import loads
from pyrogram import Client
from google_currency import convert

api_id = #
api_hash = "#"
async def main():
    async with Client("pijawca", api_id=api_id, api_hash=api_hash) as app:
        money = get('https://raw.githubusercontent.com/pijawca/changenn/master/money.txt').text
        json_object = loads(convert('rub', 'usd', int(money)))
        await app.update_profile(last_name='[' + json_object['amount'] + ']')

asyncio.run(main())
