import calendar
from cachecontrol.heuristics import BaseHeuristic
from datetime import datetime, timedelta
from email.utils import parsedate, formatdate
import requests
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache
import time


class CustomHeuristic(BaseHeuristic):

    def __init__(self, days: float = ...):
        self.days = days

    def update_headers(self, response):
        date = parsedate(response.headers['date'])
        expires = datetime(*date[:6]) + timedelta(seconds=self.days)
        print(formatdate(calendar.timegm(expires.timetuple())))
        return {
            'expires': formatdate(calendar.timegm(expires.timetuple())),
            'cache-control': 'public',
        }

    def warning(self, response):
        msg = 'Automatically cached! Response is Stale.'
        return '110 - "%s"' % msg


class CacheControlHelper(object):

    def __init__(self):
        self.sess = CacheControl(requests.session(), heuristic=CustomHeuristic(days=30), cache=FileCache('.web_cache'))

    def get(self, url):
        return self.sess.get(url)


def test_case():
    url0 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192855&domain=Procedure'
    url1 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192853&domain=Procedure'
    url2 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192854&domain=Procedure'

    req = CacheControlHelper()

    t = time.time()
    r = req.get(url0)
    print(time.time() - t)
    print(r.from_cache)
    t = time.time()
    r = req.get(url1)
    print(time.time() - t)
    print(r.from_cache)
    t = time.time()
    r = req.get(url2)
    print(time.time() - t)
    print(r.from_cache)


if __name__ == '__main__':
    test_case()

