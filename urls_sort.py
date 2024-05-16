"""Sorts URLs in a text file."""

import tldextract
from urllib.parse import urlparse

tld_extract = tldextract.TLDExtract(cache_dir=False)


def custom_sort_key(url_info: dict):
    """
    Custom function to generate sorting keys for URLs.

    Args:
    - url_info (dict): A dictionary containing the 'url' key representing URL information.

    Returns:
    - tuple: A tuple containing sorting information for the list of URLs.
    """
    url: str = url_info['url']
    tld_info = tld_extract(url)
    path = urlparse(url).path
    subdomain_key = tld_info.subdomain
    if tld_info.subdomain == '' or tld_info.subdomain == 'www':
        subdomain_key = '0'
    return (tld_info.domain, tld_info.suffix, subdomain_key, path)


def urls_sort(filepath: str):
    """
    Sorts URLs in a text file and writes the result back to the original file.

    Args:
    - filepath (str): The path of the text file to be sorted.
    """
    urls = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith('http'):
                url = {'url': line}
                if i < len(lines) - 1 and lines[i + 1].strip().startswith('<!'):
                    url['comment'] = lines[i + 1].strip()
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
                f.write(urls[i]['comment'] + '\n')


if __name__ == '__main__':
    urls_sort('urls.md')
