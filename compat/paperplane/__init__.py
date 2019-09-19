# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot initialization. """

import os

from sys import version_info
from telethon.sessions import StringSession
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb

from sample_config import Config
import pylast
from dotenv import load_dotenv
from requests import get
from telethon import TelegramClient

load_dotenv("config.env")

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    LOGS.error("You MUST have a python version of at least 3.6."
               "Multiple features depend on this. Bot quitting.")
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.error(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

# Telegram App KEY and HASH
API_KEY = Config.APP_ID
API_HASH = Config.API_HASH

# Userbot Session String
STRING_SESSION = Config.HU_STRING_SESSION

# Logging channel/group configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", "0"))

BOTLOG = sb(os.environ.get("BOTLOG", "False"))

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)

# remove.bg API key
REM_BG_API_KEY = Config.REM_BG_API_KEY

# Chrome Driver and Headless Google Chrome Binaries
CHROME_DRIVER = Config.CHROME_DRIVER
GOOGLE_CHROME_BIN = Config.GOOGLE_CHROME_BIN

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = Config.OPEN_WEATHER_MAP_APPID

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))

ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = Config.YOUTUBE_API_KEY

# Default .alive name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("TZ", None))

TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)

LASTFM_API = os.environ.get("LASTFM_API", None)
LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = pylast.md5(LASTFM_PASSWORD_PLAIN)
if not LASTFM_USERNAME == "None":
    lastfm = pylast.LastFMNetwork(api_key=LASTFM_API,
                                  api_secret=LASTFM_SECRET,
                                  username=LASTFM_USERNAME,
                                  password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_CLIENT_ID = Config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = Config.AUTH_TOKEN_DATA
GDRIVE_FOLDER_ID = Config.GDRIVE_FOLDER_ID
TEMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)

# Global Variables
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
ENABLE_KILLME = True
CMD_HELP = {}
ISAFK = False
AFKREASON = None
