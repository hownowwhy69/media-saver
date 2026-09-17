import asyncio
import importlib, MultiSaver
from pyrogram import idle 
from MultiSaver.modules import ALL_MODULES

loop = asyncio.get_event_loop()

async def init_bot():
    await MultiSaver.app.start()
    print("[√] Bot Started")
    
    getme = await MultiSaver.app.get_me()
    MultiSaver.BOT_ID = getme.id
    MultiSaver.BOT_USERNAME = getme.username
    MultiSaver.BOT_NAME = f"{getme.first_name} {getme.last_name}" if getme.last_name else getme.first_name
    print(f"»» Booted as {MultiSaver.BOT_NAME} (@{MultiSaver.BOT_USERNAME})")
  
# ------------------------------- LOAD MODULES ------------------------------- #
    for all_module in ALL_MODULES:
        importlib.import_module("MultiMedia.modules." + all_module)

    print("[√] Bot Deploy Successful ✨")
    await idle()
    await MultiSaver.app.stop()
    print("Bot Stopped!!")


if __name__ == "__main__":
    loop.run_until_complete(init_bot())
