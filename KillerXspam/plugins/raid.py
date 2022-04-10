
import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from KillerXspam import KILL, KILL2, KILL3, KILL4, KILL5 , KILL6, KILL7, KILL8, KILL9, KILL10, KILL11, KILL12, KILL13, KILL14, KILL15, KILL16, KILL17, KILL18, KILL19, KILL20, KILL21, KILL22, KILL23, KILL24, KILL25, KILL26, KILL27, KILL28, KILL29, KILL30, KILL31, KILL32, KILL33, KILL34, KILL35, KILL36, KILL37, KILL38, KILL39, KILL40, SUDO_USERS
from resources.data import RAID, REPLYRAID, KILLERSPAM
from .. import CMD_HNDLR as hl

que = {}

@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n`.raid` <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Killer = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Killer) == 2:
            user = str(K[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in KILLERSPAM:
                text = f"I can't raid on @AMAN_GURJAR_XD's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Killer[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in KILLERSPAM:
                text = f"I can't raid on @AMAN_GURJAR_XD's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Killer[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@KILL.on(events.NewMessage(incoming=True))
@KILL2.on(events.NewMessage(incoming=True))
@KILL3.on(events.NewMessage(incoming=True))
@KILL4.on(events.NewMessage(incoming=True))
@KILL5.on(events.NewMessage(incoming=True))
@KILL6.on(events.NewMessage(incoming=True))
@KILL7.on(events.NewMessage(incoming=True))
@KILL8.on(events.NewMessage(incoming=True))
@KILL9.on(events.NewMessage(incoming=True))
@KILL10.on(events.NewMessage(incoming=True))
@KILL11.on(events.NewMessage(incoming=True))
@KILL12.on(events.NewMessage(incoming=True))
@KILL13.on(events.NewMessage(incoming=True))
@KILL14.on(events.NewMessage(incoming=True))
@KILL15.on(events.NewMessage(incoming=True))
@KILL16.on(events.NewMessage(incoming=True))
@KILL17.on(events.NewMessage(incoming=True))
@KILL18.on(events.NewMessage(incoming=True))
@KILL19.on(events.NewMessage(incoming=True))
@KILL20.on(events.NewMessage(incoming=True))
@KILL21.on(events.NewMessage(incoming=True))
@KILL22.on(events.NewMessage(incoming=True))
@KILL23.on(events.NewMessage(incoming=True))
@KILL24.on(events.NewMessage(incoming=True))
@KILL25.on(events.NewMessage(incoming=True))
@KILL26.on(events.NewMessage(incoming=True))
@KILL27.on(events.NewMessage(incoming=True))
@KILL28.on(events.NewMessage(incoming=True))
@KILL29.on(events.NewMessage(incoming=True))
@KILL30.on(events.NewMessage(incoming=True))
@KILL31.on(events.NewMessage(incoming=True))
@KILL32.on(events.NewMessage(incoming=True))
@KILL33.on(events.NewMessage(incoming=True))
@KILL34.on(events.NewMessage(incoming=True))
@KILL35.on(events.NewMessage(incoming=True))
@KILL36.on(events.NewMessage(incoming=True))
@KILL37.on(events.NewMessage(incoming=True))
@KILL38.on(events.NewMessage(incoming=True))
@KILL39.on(events.NewMessage(incoming=True))
@KILL40.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sreplyraid(?: |$)(.*)" % hl))
async def _(e):
    global que
    usage = f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Killer = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        KILLx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Killer[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in KILLERSPAM:
                text = f" can't raid on @AMAN_GURJAR_XD's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                nobi = que.get(user_id)
                nobita = [user_id]
                nobi.append(nobita)
                text = f"Activated replyraid 🔥"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in KILLERSPAM:
                text = f" can't raid on @AMAN_GURJAR_XD's Owner."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                nobi = que.get(user_id)
                nobita = [user_id]
                nobi.append(nobita)
                text = f"Activated Replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sdreplyraid(?: |$)(.*)" % hl))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Killer = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Killer[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid ☑️"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    



@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sdelayraid(?: |$)(.*)" % hl))
async def _(event):
   usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗘𝗟𝗔𝗬𝗥𝗔𝗜𝗗\n\nCommand:\n\n.delayraid <delay> <count> <Username of User>\n\n.delayraid <delay> <count> <reply to a User>\n\nCount must be a integer."        
   if event.sender_id in SUDO_USERS:
         if event.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
         Killer = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
         if len(Killer) == 3:
             user = str(Killer[2])
             a = await event.client.get_entity(user)
             e = a.id
             if int(e) in KILLERSPAM:
                    text = f"I can't raid on @AMAN_GURJAR-_XD's Owner"
                    await event.reply(text, parse_mode=None, link_preview=None )
             elif int(e) in SUDO_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text, parse_mode=None, link_preview=None )
             else:
                 c = a.first_name
                 username = f"[{c}](tg://user?id={e})"
                 counter = int(Killer[1])
                 sleeptimet = sleeptimem = float(Killer[0])
                 for _ in range(counter):
                      reply = random.choice(RAID)
                      caption = f"{username} {reply}"
                      async with event.client.action(event.chat_id, "typing"):
                          await event.client.send_message(event.chat_id, caption)
                          await asyncio.sleep(sleeptimem)
         elif event.reply_to_msg_id:
               a = await event.get_reply_message()
               b = await event.client.get_entity(a.sender_id)
               e = b.id
               if int(e) in KILLERSPAM:
                       text = f"I can't raid on @AMAN_GURJAR-_XD's Owner"
                       await event.reply(text, parse_mode=None, link_preview=None )
               elif int(e) in SUDO_USERS:
                       text = f"This guy is a sudo user."
                       await event.reply(text, parse_mode=None, link_preview=None )
               else:
                   c = b.first_name
                   username = f"[{c}](tg://user?id={e})"
                   sleeptimet = sleeptimem = float(Killer[0])
                   counter = int(Killer[1])
                   for _ in range(counter):
                        reply = random.choice(RAID)
                        caption = f"{username} {reply}"
                        async with event.client.action(event.chat_id, "typing"):
                             await event.client.send_message(event.chat_id, caption)
                             await asyncio.sleep(sleeptimem)
         else:
            await event.reply(usage)
 
