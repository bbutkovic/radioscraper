from datetime import datetime
from requests import Request
from radio.utils.normalize import split_artist_title


def _timestamp():
    return int(datetime.now().timestamp() * 1000)


def form_request():
    url = 'http://streaming.goldfm.hr/stream/now_playing.php'

    return Request("GET", url, params={
        'the_stream': 'http://94.130.66.170:8068/;',
        '_': _timestamp(),
    })


def parse_response(response):
    return split_artist_title(response.text)
