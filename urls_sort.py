import tldextract
from urllib.parse import urlparse

tld_extract = tldextract.TLDExtract(cache_dir=False)


def custom_sort_key(url_info: dict):
    url: str = url_info['url']
    tld_info = tld_extract(url)
    path = urlparse(url).path
    subdomain_key = tld_info.subdomain
    if tld_info.subdomain == '' or tld_info.subdomain == 'www':
        subdomain_key = '0'
    return (tld_info.domain, tld_info.suffix, subdomain_key, path)


def urls_sort(filepath: str):
    urls = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line and not line.startswith('#') and not line.startswith('<!'):
                url = {'url': line}
                if i < len(lines) and lines[i + 1].startswith('<!'):
                    url['comment'] = lines[i + 1]
                urls.append(url)

    urls.sort(key=custom_sort_key)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('# URLs\n')
        for i in range(len(urls)):
            current_tld_info = tld_extract(urls[i]['url'])
            current_first_letter = current_tld_info.domain[0]
            previous_tld_info = None
            if i > 0:
                previous_tld_info = tld_extract(urls[i - 1]['url'])
            previous_first_letter = None
            if previous_tld_info:
                previous_first_letter = previous_tld_info.domain[0]
            if current_first_letter != previous_first_letter:
                f.write('\n')
                f.write('## ' + current_first_letter + '\n\n')
            if current_first_letter == previous_first_letter and current_tld_info.domain != previous_tld_info.domain:
                f.write('\n')
            f.write(urls[i]['url'] + '\n')
            if 'comment' in urls[i]:
                f.write(urls[i]['comment'])


if __name__ == '__main__':
    urls_sort('urls.md')
