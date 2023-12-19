def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_phi(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count

def euler_theorem(a, n):
    if gcd(a, n) != 1:
        raise ValueError("a and n must be coprime for Euler's theorem.")
    
    result = pow(a, euler_phi(n), n)
    return result

# 示例
n = 15
print(f"欧拉函数 phi({n}): {euler_phi(n)}")
# 欧拉函数 phi(15): 8

a = 7
result = euler_theorem(a, n)
print(f"欧拉定理: {a}^phi({n}) mod {n} = {result}")