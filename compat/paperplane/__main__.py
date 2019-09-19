""" Userbot start point """

from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot
from stdplugins.ppeplugins import ALL_MODULES


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("stdplugins.ppeplugins." + module_name)

LOGS.info("Your userbot version is 4.0 - Extended")

LOGS.info(
    "Congratulations, your userbot is now running !! Test it by typing .alive in any chat."
    "If you need assistance, head to https://t.me/PaperplaneExtendedChat")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
