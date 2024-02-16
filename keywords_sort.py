"""Sort keywords in a text file."""


def keywords_sort(filepath: str):
    keywords = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            keywords.append(line)

    keywords.sort()
    print(len(keywords))

    with open(filepath, 'w', encoding='utf-8') as f:
        for keyword in keywords:
            f.write(keyword + '\n')


if __name__ == '__main__':
    keywords_sort('keywords.txt')
