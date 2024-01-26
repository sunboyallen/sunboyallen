import tldextract
from urllib.parse import urlparse

tld_extract = tldextract.TLDExtract(cache_dir=False)

urls = []

with open('urls.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        if line and not line.startswith('#') and not line.startswith('<!'):
            url = {'url': line}
            if i < len(lines) - 1 and lines[i + 1].startswith('<!'):
                url['comment'] = lines[i + 1]
            urls.append(url)


def custom_sort_key(url_info: dict):
    url: str = url_info['url']
    tld_info = tld_extract(url)
    path: str = urlparse(url).path
    subdomain_key = tld_info.subdomain
    if tld_info.subdomain == '' or tld_info.subdomain == 'www':
        subdomain_key = '0'
    return (tld_info.domain, subdomain_key, tld_info.suffix, path)


urls.sort(key=custom_sort_key)

with open('urls.md', 'w', encoding='utf-8') as f:
    f.write('# URLs\n')
    previous_first_letter = None

    for i in range(len(urls)):
        tld_info = tld_extract(urls[i]['url'])
        current_first_letter = tld_info.domain[0] if tld_info.domain else None

        if current_first_letter != previous_first_letter:
            f.write('\n')
            f.write('## ' + current_first_letter + '\n\n')

        if i > 0:
            tld_info1 = tld_extract(urls[i - 1]['url'])
            tld_info2 = tld_extract(urls[i]['url'])
            if tld_info1.domain != tld_info2.domain and tld_info1.domain[0] == tld_info2.domain[0]:
                f.write('\n')

        f.write(urls[i]['url'] + '\n')
        if 'comment' in urls[i]:
            f.write(urls[i]['comment'])

        previous_first_letter = current_first_letter
