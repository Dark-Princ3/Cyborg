""" For .yt command, do a YouTube search from Telegram. """
    

from uniborg.util import admin_cmd
from telethon import events
from googleapiclient.discovery import build
from pytube import YouTube
from pytube.helpers import safe_filename


@borg.on(admin_cmd("yt ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        query = event.pattern_match.group(1)
        result = ''
        i = 1

        if Config.YOUTUBE_API_KEY is None:
            await event.edit("`Error: YouTube API key missing! Add it in HEROKU Config Vars`")
            return

        await event.edit("```Processing...```")

        full_response = youtube_search(query)
        videos_json = full_response[1]


        for video in videos_json:
            result += f"{i}. {video['snippet']['title']} \
                \nhttps://www.youtube.com/watch?v={video['id']['videoId']}\n"
            i += 1

        reply_text = f"**Search Query:**\n`{query}`\n\n**Result:**\n{result}"

        await event.edit(reply_text)


def youtube_search(
        query,
        order="relevance",
        token=None,
        location=None,
        location_radius=None
    ):

    """ Do a YouTube search. """
    youtube = build('youtube', 'v3',
                    developerKey=Config.YOUTUBE_API_KEY, cache_discovery=False)
    search_response = youtube.search().list(
        q=query,
        type="video",
        pageToken=token,
        order=order,
        part="id,snippet",
        maxResults=10,
        location=location,
        locationRadius=location_radius
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return(nexttok, videos)
    except HttpError:
        nexttok = "last_page"
        return(nexttok, videos)
    except KeyError:
        nexttok = "KeyError, try again."
        return(nexttok, videos)
