async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import random
import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from KillerXspam import KILL, KILL2, KILL3, KILL4, KILL5 , KILL6, KILL7, KILL8, KILL9, KILL10, KILL11, KILL12, KILL13, KILL14, KILL15, KILL16, KILL17, KILL18, KILL19, KILL20, KILL21, KILL22, KILL23, KILL24, KILL25, KILL26, KILL27, KILL28, KILL29, KILL30, KILL31, KILL32, KILL33, KILL34, KILL35, KILL36, KILL37, KILL38, KILL39, KILL40, SUDO_USERS
from .. import CMD_HNDLR as hl
from resources.data import KILLERSPAM, PORNSPAM, GROUP

que = {}


# spam

@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Killer = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Killer) == 2:
            message = str(Killer[1])
            counter = int(Killer[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Killer[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Killer[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


#bigspam

@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Killer = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Killer) == 2:
            message = str(Killer[1])
            counter = int(Killer[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(Killer[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Killer[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#abuse



@KILL.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
async def pspam(e):
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        amanop = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(amanop) == 1:
            counter = int(amanop[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORNSPAM)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            usage = f"**MODULE NAME : PORN SPAM** \n\n command: `{hl}pornspam <count>`"
            await e.reply(usage, parse_mode=None, link_preview=None )



