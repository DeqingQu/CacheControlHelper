# CacheControl Helper for time-based requests

CacheControl is an extension that adds a full HTTP cache to Requests. https://cachecontrol.readthedocs.io/en/latest/

CacheControlHelper is a helper class for CacheControl using time based and file based caching strategy.

The request will be cached in the '.web_cache' directory for 30 days.

Required Modules:
<pre><code>pip3 install requests, CacheControl, lockfile
</code></pre>

Demo:
<pre><code>def get_request(url):
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
</code></pre>
