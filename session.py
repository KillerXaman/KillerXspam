from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print(
    """KILLER SQUAD SPAM BOT"""
)

print("\n • Telethon Session •")

print("\n\nEnter Your Valid Details To Continue!\n\n")

        
APP_ID = int(input("\nEnter APP ID here: "))
API_HASH = input("\nEnter API HASH here: ")


try:
   with TelegramClient(StringSession(), APP_ID, API_HASH) as Killer:
       print("\nSTRING SESSION GENERATE SUCCESSFULLY CHECK SAVED MASSAGE")
       Killer.send_message("me", f"**Killer X Spam Session :**\n\n`{Killer.session.save()}`\n\n__Do not share this anywhere!!__")
       
except Exception as e:
    print(f"{e}")
