# CacheControl Helper for time-based requests

CacheControl is an extension that adds a full HTTP cache to Requests. https://cachecontrol.readthedocs.io/en/latest/

CacheControlHelper is a helper class for CacheControl using time based and file based caching strategy.

The request will be cached in the '.web_cache' directory for 30 days.

Required Modules:
<pre><code>pip3 install requests, CacheControl, lockfile
</code></pre>

Demo:
<pre><code>req = CacheControlHelper()
res = req.get('http://google.com')
assert res.from_cache
</code></pre>