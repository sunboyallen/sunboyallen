import tldextract

url = "https://yun.ggo.net/"

# extracted_info = tldextract.extract(url)

tld_extract = tldextract.TLDExtract(cache_dir=False)
extracted_info = tld_extract(url)

print(extracted_info.domain)
print(extracted_info.subdomain)
print(extracted_info.suffix)
