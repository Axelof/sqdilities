import maxminddb
from aiohttp import ClientSession

from sqdilities.definitions import files_directory, geo_file


async def external_address():
    async with ClientSession() as session:
        async with session.get("https://api.ipify.org?format=json") as response:
            external = await response.json()
    return external['ip']


def locate(ip_address: str):
    if not geo_file.exists():
        raise FileNotFoundError(f"""
        No geo.mmdb found at {files_directory}
        install package with `geo` option and use cli command `sqdilities install geo`
        """)

    with maxminddb.open_database(files_directory / "geo.mmdb") as reader:
        entry = reader.get(ip_address)
    return entry
