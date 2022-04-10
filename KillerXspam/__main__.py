
import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from KillerXspam.utils import load_plugins
import logging
from telethon import events
from . import KILL, KILL2, KILL3, KILL4, KILL5 , KILL6, KILL7, KILL8, KILL9, KILL10, KILL11, KILL12, KILL13, KILL14, KILL15, KILL16, KILL17, KILL18, KILL19, KILL20, KILL21, KILL22, KILL23, KILL24, KILL25, KILL26, KILL27, KILL28, KILL29, KILL30, KILL31, KILL32, KILL33, KILL34, KILL35, KILL36, KILL37, KILL38, KILL39, KILL40

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "KillerXspam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("💯💞 𝙺𝙸𝙻𝙻𝙴𝚁 𝚂𝚀𝚄𝙰𝙳 𝚂𝙿𝙰𝙼 𝙱𝙾𝚃 𝚂𝚄𝙲𝙲𝙴𝚂𝙵𝚄𝙻𝙻𝚈 𝙳𝙴𝙿𝙻𝙾𝚈𝙴𝙳 💯💞")
print("𝙴𝙽𝙹𝙾𝚈! 𝙳𝙾 𝚅𝙸𝚂𝙸𝚃 @KillerSquad")

if len(argv) not in (1, 3, 4):
    try:
        KILL.disconnect()
    except Exception as e:
        pass
    try:
        KILL2.disconnect()
    except Exception as e:
        pass
    try:
        KILL3.disconnect()
    except Exception as e:
        pass
    try:
        KILL4.disconnect()
    except Exception as e:
        pass
    try:
        KILL5.disconnect()
    except Exception as e:
        pass
    try:
        KILL6.disconnect()
    except Exception as e:
        pass
    try:
        KILL7.disconnect()
    except Exception as e:
        pass
    try:
        KILL8.disconnect()
    except Exception as e:
        pass
    try:
        KILL9.disconnect()
    except Exception as e:
        pass
    try:
        KILL10.disconnect()
    except Exception as e:
        pass
    try:
        KILL11.disconnect()
    except Exception as e:
        pass
    try:
        KILL12.disconnect()
    except Exception as e:
        pass
    try:
        KILL13.disconnect()
    except Exception as e:
        pass
    try:
        KILL14.disconnect()
    except Exception as e:
        pass
    try:
        KILL15.disconnect()
    except Exception as e:
        pass
    try:
        KILL16.disconnect()
    except Exception as e:
        pass
    try:
        KILL17.disconnect()
    except Exception as e:
        pass
    try:
        KILL18.disconnect()
    except Exception as e:
        pass
    try:
        KILL19.disconnect()
    except Exception as e:
        pass
    try:
        KILL20.disconnect()
    except Exception as e:
        pass
    try:
        KILL21.disconnect()
    except Exception as e:
        pass
    try:
        KILL22.disconnect()
    except Exception as e:
        pass
    try:
        KILL23.disconnect()
    except Exception as e:
        pass
    try:
        KILL24.disconnect()
    except Exception as e:
        pass
    try:
        KILL25.disconnect()
    except Exception as e:
        pass
    try:
        KILL26.disconnect()
    except Exception as e:
        pass
    try:
        KILL27.disconnect()
    except Exception as e:
        pass
    try:
        KILL28.disconnect()
    except Exception as e:
        pass
    try:
        KILL29.disconnect()
    except Exception as e:
        pass
    try:
        KILL30.disconnect()
    except Exception as e:
        pass
    try:
        KILL31.disconnect()
    except Exception as e:
        pass
    try:
        KILL32.disconnect()
    except Exception as e:
        pass
    try:
        KILL33.disconnect()
    except Exception as e:
        pass
    try:
        KILL34.disconnect()
    except Exception as e:
        pass
    try:
        KILL35.disconnect()
    except Exception as e:
        pass
    try:
        KILL36.disconnect()
    except Exception as e:
        pass
    try:
        KILL37.disconnect()
    except Exception as e:
        pass
    try:
        KILL38.disconnect()
    except Exception as e:
        pass
    try:
        KILL39.disconnect()
    except Exception as e:
        pass
    try:
        KILL40.disconnect()
    except Exception as e:
        pass
else:
    try:
        KILL.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL2.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL3.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL4.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL5.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL6.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL7.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL8.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL9.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL10.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL11.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL12.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL13.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL14.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL15.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL16.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL17.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL18.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL19.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL20.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL21.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL22.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL23.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL24.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL25.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL26.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL27.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL28.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL29.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL30.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL31.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL32.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL33.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL34.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL35.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL36.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL37.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL38.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL39.run_until_disconnected()
    except Exception as e:
        pass
    try:
        KILL40.run_until_disconnected()
    except Exception as e:
        pass
