from telethon import TelegramClient

name = 'name_API_Telegram'
api_id = 'api_id telegram'
api_hash ='api_hash telegram'
client = TelegramClient(name, api_id, api_hash)

async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'halo perkenalkan aku bot scrapping')
    await client.send_message('me', 'Apa yang ingin kami butuhkan???')
    await client.send_message('me', 'Salam kenal saya AI Raffli Siap membantu anda!!!')

with client:
    client.loop.run_until_complete(main())