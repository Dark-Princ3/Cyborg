# uniborg

Pluggable [``asyncio``](https://docs.python.org/3/library/asyncio.html)
[Telegram](https://telegram.org) userbot based on
[Telethon](https://github.com/LonamiWebs/Telethon).

## installing

#### The Easy Ways

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### The Legacy Way
Simply clone the repository and run the main file:
```sh
git clone https://github.com/uniborg/uniborg.git
cd uniborg
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py with variables as given below>
python3 -m stdborg
```

An example `config.py` file could be:

**Not All of the variables are mandatory**

__The UniBorg should work by setting only the first two variables__

```python3
from sample_config import Config

class Development(Config):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN_BF_HER = ""
  PPE_MODE = "False" # Set to "True" to activate PaperPlaneExtended. Leave "False" to activate CyBorg
  TG_BOT_USER_NAME_BF_HER = ""
  UB_BLACK_LIST_CHAT = []
  # chat ids or usernames, it is recommended to use chat ids,
  # providing usernames means an additional overhead for the user
  CHATS_TO_MONITOR_FOR_ANTI_FLOOD = []
  # specify LOAD and NO_LOAD
  LOAD = []
  NO_LOAD = []
```

## internals

The core features offered by the custom `TelegramClient` live under the
[`uniborg/`](https://github.com/SpEcHiDe/uniborg/tree/master/uniborg)
directory, with some utilities, enhancements, the `_core` plugin, and the `_inline_bot` plugin.


## [Mandatory Vars]

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will work without setting the non-mandatory environment variables.
- Please report any issues to the support group: [@SpEcHlDe](https://t.me/joinchat/AHAujEjG4FBO-TH-NrVVbg)


## design

The modular design of the project enhances your Telegram experience
through `PLUGINS` which you can enable or disable on demand.

Each plugin gets the `borg`, `logger`, `Config`, `tgbot` magical
[variables](https://github.com/Total-Noob-69/UniBorg/blob/488eff632e65103ba7017d4f52777d22ddd52ea2/uniborg/uniborg.py#L76-L80)
to ease their use. Thus creating a plugin as easy as adding
a new file under the plugin directory to do the job:

```python
# stdplugins/myplugin.py
from telethon import events
from uniborg.util import admin_cmd
@borg.on(admin_cmd(pattern="hi"))
async def handler(event):
    await event.reply("hey")
```


## learning

Check out the already-mentioned [plugins](https://github.com/Total-Noob-69/UniBorg/tree/master/stdplugins) directory, or some third-party [plugins](https://telegram.dog/UniBorg) to learn how to write your own, and consider reading [Telethon's documentation](http://telethon.readthedocs.io/).


## credits


Thanks to:
- [lonami](https://lonami.dev) for creating [Telethon](https://github.com/lonamiwebs/Telethon)
- [![CopyLeft](https://telegra.ph/file/b514ed14d994557a724cb.jpg)](https://telegra.ph/file/fab1017e21c42a5c1e613.mp4 "CopyLeft Credit Video")
