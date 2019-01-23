from cache_control_helper import CacheControlHelper
import time
import sys


def get_request(url):
    requests = CacheControlHelper()
    try:
        res = requests.get(url, timeout=120)
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


if __name__ == '__main__':
    base_url = 'http://localhost:3000/test/'
    t = time.time()
    for i in range(100000):
        r = get_request(base_url + str(i))
        if i % 1000 == 0:
            print(r)
            print(time.time() - t)
    print(time.time() - t)
