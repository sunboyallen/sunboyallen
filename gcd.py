def gcd(m: int, n: int) -> int:
    return m if n == 0 else gcd(n, m % n)


if __name__ == '__main__':
    m = int(input('请输入第一个整数: '))
    n = int(input('请输入第二个整数: '))
    print('最大公约数为: ', gcd(m, n))
