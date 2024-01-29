"""Sort keywords in a text file."""


def keywords_sort(filepath: str):
    keywords = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                keywords.append(line)

    keywords.sort()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('# Keywords\n\n')
        for keyword in keywords:
            f.write(keyword + '\n\n')


if __name__ == '__main__':
    keywords_sort('keywords.md')
