import calendar
from cachecontrol.heuristics import BaseHeuristic
from datetime import datetime, timedelta
from email.utils import parsedate, formatdate
from requests import Session
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache
import time


class CustomHeuristic(BaseHeuristic):

    def __init__(self, days: float = ..., seconds: float = ..., minutes: float = ..., hours: float = ...):
        self.days = days
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def update_headers(self, response):
        date = parsedate(response.headers['date'])
        expires = datetime(*date[:6]) + timedelta(seconds=self.seconds)
        return {
            'expires': formatdate(calendar.timegm(expires.timetuple())),
            'cache-control': 'public',
        }

    def warning(self, response):
        msg = 'Automatically cached! Response is Stale.'
        return '110 - "%s"' % msg


if __name__ == '__main__':
    url0 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192855&domain=Procedure'
    url1 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192853&domain=Procedure'
    url2 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192854&domain=Procedure'

    sess = CacheControl(Session(), heuristic=CustomHeuristic(seconds=30), cache=FileCache('.web_cache'))

    t = time.time()
    r = sess.get(url1)
    print(time.time() - t)
    print(r.from_cache)
    t = time.time()
    r = sess.get(url1)
    print(time.time() - t)
    print(r.from_cache)
    t = time.time()
    r = sess.get(url1)
    print(time.time() - t)
    print(r.from_cache)

