from cache_control_helper import CacheControlHelper
import time

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