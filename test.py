print("ok")

import tldextract

tld_extract = tldextract.TLDExtract(cache_dir=None)

print(tld_extract('http://115.182.62.169:8000/'))
