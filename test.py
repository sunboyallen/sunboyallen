print("ok")

import tldextract

tld_extract = tldextract.TLDExtract(cache_dir=False)

url = "https://baidu.com/test"

tld_info = tld_extract(url)

print(tld_info.subdomain)