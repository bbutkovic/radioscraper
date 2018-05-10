from datetime import datetime
from requests import Request
from radio.utils.normalize import split_artist_title


def _timestamp():
    return int(datetime.now().timestamp() * 1000)


def form_request():
    url = 'http://streaming.antenazagreb.hr/stream/now_playing.php'

    return Request("GET", url, params={
        'the_stream': 'http://live.antenazagreb.hr:8000/;',
        '_': _timestamp(),
    })


def parse_response(response):
    return split_artist_title(response.text)
