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


def get_request_with_cookie(url):
    API_KEY = '1YCxuN7PRHyrpuZnO7F5gQ'
    API_BASE_URL = 'https://api.omim.org/api'

    session_data = {'apiKey': API_KEY,
                    'format': 'json'}

    requests = CacheControlHelper()
    r = requests.sess.post(API_BASE_URL + "/apiKey", data=session_data)
    assert 200 == r.status_code
    cookie = r.cookies

    try:
        res = requests.get(url, cookies=cookie)
    except requests.exceptions.Timeout:
        print(url, file=sys.stderr)
        print("Timeout in QueryOMIM for URL: " + url, file=sys.stderr)
        return None
    except BaseException as e:
        print(url, file=sys.stderr)
        print('%s received in QueryOMIM for URL: %s' % (e, url), file=sys.stderr)
        return None
    status_code = res.status_code
    if status_code != 200:
        print("Status code " + str(status_code) + " for URL: " + url, file=sys.stderr)
        return None
    return res.json()


url0 = 'http://cohd.io/api/association/obsExpRatio?datset_id=1&concept_id_1=192855&domain=Procedure'
url1 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192853&domain=Procedure'
url2 = 'https://flippingbook.com/404'
url3 = 'https://www.google.com:81'
url4 = 'https://api.omim.org/api/entry?mimNumber=166710&include=geneMap,externalLinks&exclude=text&format=json'
url5 = 'https://api.omim.org/api/entry?mimNumber=100100&include=text:description&format=json'
url6 = 'https://api.omim.org/api/entry?mimNumber=61447&include=text:description&format=json'

#   get_requests
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

#   get_request_with_cookie
t = time.time()
r = get_request_with_cookie(url4)
print(time.time() - t)
print(r)
t = time.time()
r = get_request_with_cookie(url5)
print(time.time() - t)
print(r)
t = time.time()
r = get_request_with_cookie(url6)
print(time.time() - t)
print(r)