import os
import sys
import random
from os import execl
import asyncio
import telethon.utils
from KillerXspam import KILL, KILL2, KILL3, KILL4, KILL5 , KILL6, KILL7, KILL8, KILL9, KILL10, KILL11, KILL12, KILL13, KILL14, KILL15, KILL16, KILL17, KILL18, KILL19, KILL20, KILL21, KILL22, KILL23, KILL24, KILL25, KILL26, KILL27, KILL28, KILL29, KILL30, KILL31, KILL32, KILL33, KILL34, KILL35, KILL36, KILL37, KILL38, KILL39, KILL40, DEV
from .. import CMD_HNDLR as hl
from telethon.tl import functions
from telethon import events


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest, InviteToChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info      
    
            
@KILL.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL2.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL3.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL4.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL5.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL6.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL7.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL8.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL9.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL10.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL11.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL12.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL13.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL14.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL15.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL16.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL17.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL18.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL19.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL20.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL21.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL22.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL23.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL24.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL25.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL26.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL27.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL28.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL29.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL30.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL31.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL32.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL33.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL34.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL35.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL36.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL37.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL38.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL39.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@KILL40.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
async def get_users(event):
    if event.sender_id in DEV:
        Nobi = event.text[11:]
        KILLERSPAM = Nobi.lower()
        restricted = ["@KillerXspam", "@KillerSquadspambot", "@SAB_KAA_KATEGA"]
        KILLx = await event.reply("__Inviting members __")
        if KILLERSPAM in restricted:
            await KILLx.edit("You can't Invite Members from there.")
            await event.client.send_message(-1001597222229, "Sorry for inviting members from here.")
            return
        KILLER_SPAM_BOT = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await KILLx.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"
        await KILLx.edit("**INVITING USERS !!**")
        async for user in event.client.iter_participants(KILLER_SPAM_BOT.full_chat.id):
            try:
                await event.client(
                    InviteToChannelRequest(channel=chat, users=[user.id])
                )
                s += 1
                await KILLx.edit(
                    f"**INVITING USERS.. **\n\n**Invited :**  `{s}` users \n**Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
            )
            except Exception as e:
                error = str(e)
                f += 1
        return await KILLx.edit(
        f"**INVITING FINISHED** \n\n**Invited :**  `{s}` users \n**Failed :**  `{f}` users."
    )


