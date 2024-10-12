from aiohttp import ClientSession


URL = "https://api.ipify.org?format=json"


async def external_address():
    async with ClientSession() as session:
        async with session.get(URL) as response:
            external = await response.json()
    return external['ip']
