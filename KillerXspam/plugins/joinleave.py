import asyncio
from KillerXspam import KILL, KILL2, KILL3, KILL4, KILL5 , KILL6, KILL7, KILL8, KILL9, KILL10, KILL11, KILL12, KILL13, KILL14, KILL15, KILL16, KILL17, KILL18, KILL19, KILL20, KILL21, KILL22, KILL23, KILL24, KILL25, KILL26, KILL27, KILL28, KILL29, KILL30, KILL31, KILL32, KILL33, KILL34, KILL35, KILL36, KILL37, KILL38, KILL39, KILL40, SUDO_USERS
from .. import CMD_HNDLR as hl
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events
import os
import random
import sys


@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sjoin(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SUDO_USERS:
        KILLERSPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = KILLERSPAM[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Joined Successfully ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@KILL.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%spjoin(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/abcdefghijklmsnob\n\n.pjoin abcdefghijklmsnob"
    if e.sender_id in SUDO_USERS:
        KILLERSPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = KILLERSPAM[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Joined Successfully (Private Group/channel) ✅")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



#leave 
@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SUDO_USERS:
        KILLERSPAM = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = KILLERSPAM[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left ☑️")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )   

