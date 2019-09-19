""" Google Translate
Available Commands:
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate"""

import emoji
import asyncio
from googletrans import Translator
from uniborg.util import admin_cmd


@borg.on(admin_cmd("tr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        lan, text = input_str.split("|")
        pet = True
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
        pet = False
    else:
        await event.edit("`.tr LanguageCode` as reply to a message")
        return
    lan = lan.strip()
    translator = Translator()
    try:
        text = emoji.demojize(text.strip())
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        if pet:
            output_str = after_tr_text
        else:
            output_str = """**TRANSLATED** from {} to {}\n{}""".format(
                translated.src,
                lan,
                after_tr_text
            )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))
