import asyncio
import os
from pathlib import Path
import base64
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from KillerXspam import KILL, KILL2, KILL3, KILL4, KILL5 , KILL6, KILL7, KILL8, KILL9, KILL10, KILL11, KILL12, KILL13, KILL14, KILL15, KILL16, KILL17, KILL18, KILL19, KILL20, KILL21, KILL22, KILL23, KILL24, KILL25, KILL26, KILL27, KILL28, KILL29, KILL30, KILL31, KILL32, KILL33, KILL34, KILL35, KILL36, KILL37, KILL38, KILL39, KILL40, SUDO_USERS, DEV
from .. import CMD_HNDLR as hl
from telethon import events
from telethon.tl.types import Channel, Chat, InputPhoto, User
from telethon import events, version
from KillerXspam import ALIVE_PIC, killerversion


#name    
    
@KILL.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%ssetname(?: |$)(.*)" % hl))
async def name(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗡𝗔𝗠𝗘\n\nCommand:\n\n.setname <Message to change name of spam ids>"
    if e.sender_id in DEV:
        names = e.text.split(" ", 1)
        KILLERSPAM = names[1]
        if len(e.text) > 5:
            firstname = KILLERSPAM
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=firstname))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await event.edit("Changed name successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#bio 
            
@KILL.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%ssetbio(?: |$)(.*)" % hl))
async def _(e):
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗖𝗛𝗔𝗡𝗚𝗘 𝗕𝗜𝗢\n\nCommand:\n\n.setbio <Message to change name of spam ids>"
    if e.sender_id in DEV:
        fukyou = e.text.split(" ", 1)
        message = fukyou[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Bio..."
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed bio successfully! ✅")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )         
        

# statss                   
            
@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sstats(?: |$)(.*)" % hl))
async def stats(event):
   u = 0
   g = 0
   c = 0
   bc = 0
   b = 0
   KILLERSPAM = ""
   if event.sender_id in DEV:    
        await event.delete()
        event = await event.reply("__Processing__.....")
       # await event.edit("`Processing..`")
        dialogs = await event.client.get_dialogs(limit=None, ignore_migrated=True)
        for d in dialogs:
            currrent_entity = d.entity
            if isinstance(currrent_entity, User):
                if currrent_entity.bot:
                    b += 1
                else:
                    u += 1
            elif isinstance(currrent_entity, Chat):
                g += 1
            elif isinstance(currrent_entity, Channel):
                if currrent_entity.broadcast:
                    bc += 1
                else:
                    c += 1
            else:
                print(d)
         
        KILLERSPAM += f"💥 **ɦɛʀɛ ɨֆ ყσʊʀ ҡเℓℓε૨ sզᴜᴀᴅ sραɱ sƭαƭs** 💥\n\n"
        KILLERSPAM += f"✨ `ᴜsεʀs:`\t**{u}**\n"
        KILLERSPAM += f"💯 `ɢʀᴏᴜᴘs:`\t**{g}**\n"
        KILLERSPAM += f"🗯️ `sᴜᴘᴇʀ ɢʀᴏᴜᴘs:`\t**{c}**\n"
        KILLERSPAM += f"💞 `ᴄɦαɳɳεℓs:`\t**{bc}**\n"
        KILLERSPAM += f"🖤 `ʙᴏᴛs`\t**{b}**"
        await event.edit(KILLERSPAM)    
    
  

# ALIVE

KILL_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/c6f99c0b68ff07439ed72.jpg"


KILLER = "🚩 ҡเℓℓε૨ sqυα∂ sραɱ ɓσƭ \n\n"

KILLER += f"**💥 ƭεℓεƭɦσɳ** ☞︎︎︎ `{version.__version__}`\n\n"

KILLER += f"**💯 ҡιℓℓεя ѵεяsเσɳ** ☞︎︎︎ `{killerversion}`\n\n"

KILLER += f"**💫 sυρρσят** ☞︎︎︎ [ʝσเɳ](https://t.me/KILLERSQUAD)\n\n"

KILLER += f"**💞 υρ∂αƭεs** ☞︎︎︎ [ʝσเɳ](https://t.me/KILLERSQUADSPAMBOT)\n\n"

KILLER += f"🖤 **ʀερσ** ☞︎︎︎ [ƭαρ](https://github.com/KillerXaman/KillerXspam) 🖤"            

@KILL.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await KILL.send_file(event.chat_id,
                                  KILL_PIC,
                                  caption=KILLER
                               )
     
