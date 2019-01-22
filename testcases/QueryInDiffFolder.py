from cache_control_helper import CacheControlHelper
import time
import sys

url0 = 'http://cohd.io/api/association/obsExpRatio?datset_id=1&concept_id_1=192855&domain=Procedure'
url1 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192853&domain=Procedure'
url2 = 'https://flippingbook.com/404'
url3 = 'https://www.google.com:81'


def get_request(url):
    requests = CacheControlHelper()
    try:
        res = requests.get(url)
    except requests.exceptions.Timeout:
        print(url, file=sys.stderr)
        print('Timeout for URL: ' + url, file=sys.stderr)
        return None
    except KeyboardInterrupt:
        sys.exit(0)
    except BaseException as e:
        print(url, file=sys.stderr)
        print('%s received for URL: %s' % (e, url), file=sys.stderr)
        return None
    status_code = res.status_code
    if status_code != 200:
        print(url, file=sys.stderr)
        print('Status code ' + str(status_code) + ' for url: ' + url, file=sys.stderr)
        return None
    return res.json()


t = time.time()
r = get_request(url0)
print(time.time() - t)
print(r)
t = time.time()
r = get_request(url1)
print(time.time() - t)
print(r)
t = time.time()
r = get_request(url2)
print(time.time() - t)
print(r)
t = time.time()
r = get_request(url3)
print(time.time() - t)
print(r)