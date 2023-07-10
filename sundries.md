# 杂项

## gcd 最大公约数

```cpp
int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a % b);
}
```

## 素数筛法

### 埃氏筛法

```cpp
bool notprime[100000];
void sieve(int x = 44000)
{
    notprime[1] = 1;
    notprime[2] = 0;
    for(int i = 2; i <= x; i++)
        if(!notprime[i])
            for(int j = i; j * i <= x; j++)
                notprime[j * i] = 1;
}
```

时间复杂度为O(nloglogn)

### 欧拉筛法

```cpp
bool notprime[10000000];
int prime[10000000];
void sieve(int x = 1000003)
{
    int n = 0;
    notprime[1] = 1;
    notprime[2] = 0;
    for(int i = 1; i <= x; i++)
    {
        if(!notprime[i])
            prime[++n] = i;
        for(int j = 1; j <= n && i * prime[j] <= x; j++)
        {
            notprime[i * prime[j]] = 1;
            if(i % prime[j] == 0)
                break;
        }
    }
}
```

时间复杂度为O(n)
