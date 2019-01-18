import requests
import requests_cache
import hashlib
import time

_DEFAULT_HEADERS = requests.utils.default_headers()

requests_cache.install_cache("orangeboard")


def get_timestamp(url):
    """
    get the timestamp of an HTTP get request
    :param url: the URL of the request
    :return the timestamp of the request, of None if the request is not in the cache
    """
    def _to_bytes(s, encoding='utf-8'):
        return bytes(s, encoding)

    def create_key(request):
        url, body = request.url, request.body
        key = hashlib.sha256()
        key.update(_to_bytes(request.method.upper()))
        key.update(_to_bytes(url))
        if request.body:
            key.update(_to_bytes(body))
        return key.hexdigest()

    def url_to_key(url):
        session = requests.Session()
        return create_key(session.prepare_request(requests.Request('GET', url)))

    #   get the cache from request_cache
    results = requests_cache.get_cache()
    #   create the key according to the url
    key_url = url_to_key(url)
    #   results.responses is a dictionary and follows the following format:
    #   { 'key': (requests_cache.backends objects, timestamp), ..., }
    #   for example: '4c28e3e4a61e325e520d9c02e0caee99e30c00951a223e67':
    #                       (<requests_cache.backends.base._Store object at 0x12697e630>,
    #                           datetime.datetime(2018, 10, 16, 0, 19, 8, 130204)),
    if key_url in results.responses:
        back_obj, timestamp = results.responses[key_url]
        return timestamp
    return None


if __name__ == '__main__':

    url0 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192855&domain=Procedure'
    url1 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192853&domain=Procedure'
    url2 = 'http://cohd.io/api/association/obsExpRatio?dataset_id=1&concept_id_1=192854&domain=Procedure'

    t = time.time()
    res1 = requests.get(url1)
    print(time.time() - t)
    t = time.time()
    res1 = requests.get(url1)
    print(time.time() - t)
    t = time.time()
    res1 = requests.get(url1)
    print(time.time() - t)

    t = time.time()
    print(get_timestamp(url0))
    print(get_timestamp(url1))
    print(get_timestamp(url2))
    print("Time used: ", time.time() - t)