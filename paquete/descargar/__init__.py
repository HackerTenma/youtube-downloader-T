from __future__ import unicode_literals
import youtube_dl


def download(directory, link, my_hook=None):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': directory + ".%(ext)s",
    }
    if my_hook is not None:
        ydl_opts['progress_hooks'] = [my_hook]
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
