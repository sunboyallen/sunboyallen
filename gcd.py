def gcd(m: int, n: int) -> int:
    return m if n == 0 else gcd(n, m % n)


if __name__ == '__main__':
    print(gcd(51, 15))
