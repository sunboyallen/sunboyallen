import tldextract

tld_extract = tldextract.TLDExtract(cache_dir=False)

with open('urls.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    urls = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if line and not line.startswith('#') and not line.startswith('<!'):
            # 如果urls[i]的下一行是注释，那么将注释写在urls[i]的后面
            if i < len(lines) - 1:
                next_line = lines[i + 1]
                if next_line.startswith('<!'):
                    line = line + ' ' + next_line.strip()

            urls.append(line)

def custom_sort_key(url: str):
    tld_info = tld_extract(url)
    # 以www开头的或没有subdomain的URL排在其他的之前
    if not tld_info.subdomain or tld_info.subdomain == 'www':
        subdomain_key = '0'
    else:
        subdomain_key = tld_info.subdomain
    return (tld_info.domain, subdomain_key, tld_info.suffix)

urls.sort(key=custom_sort_key)

with open('urls.md', 'w', encoding='utf-8') as f:
    f.write('# URLs\n')
    previous_first_letter = None

    for i in range(len(urls)):
        tld_info = tld_extract(urls[i])
        current_first_letter = tld_info.domain[0] if tld_info.domain else None
        
        if current_first_letter != previous_first_letter:
            f.write('\n')
            f.write('## ' + current_first_letter + '\n\n')

        if i > 0:
            tld_info1 = tld_extract(urls[i-1])
            tld_info2 = tld_extract(urls[i])
            if tld_info1.domain != tld_info2.domain and tld_info1.domain[0] == tld_info2.domain[0]:
                f.write('\n')
        
        # 如果urls[i]包括网址和注释，以空格隔开，注释以<!开头，那么将注释写在下一行
        if '<!' in urls[i]:
            f.write(urls[i].split(' <!')[0] + '\n')
            f.write('<!' + urls[i].split(' <!')[1] + '\n')
        else:
            f.write(urls[i] + '\n')
        
        previous_first_letter = current_first_letter
