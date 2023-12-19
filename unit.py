def prime_factors(n):
    factors = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors

def euler_phi(n):
    result = n
    factors = prime_factors(n)

    for p in set(factors):
        result -= result // p

    return result

# 示例
n = 15
print(f"欧拉函数 phi({n}): {euler_phi(n)}")
