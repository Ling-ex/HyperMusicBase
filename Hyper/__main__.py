import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from geezram import LOGGER, app, userbot
from geezram.core.call import Anon
from geezram.plugins import ALL_MODULES
from geezram.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Geez|RAM").error(
            "Please add a pyrogram string..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Geez|RAM").warning(
            "Spotify vars not detected, unable to play from spotify."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("geezram.plugins." + all_module)
    LOGGER("geezram.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Anon.start()
    try:
        await Anon.stream_decall("https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4")
    except:
        pass
    try:
        await Anon.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Geez|RAM").error(
            "[ERROR] - \n\nPlease open telegram and turn on voice chat in Logger Group. If you ever ended voice chat in log group i will stop working."
        )
        sys.exit()
    except:
        pass
    await Anon.decorators()
    LOGGER("Geez|RAM").info("izzy music started")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Geez|RAM").info("Stopping Music Bot...")
