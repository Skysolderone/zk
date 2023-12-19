def extended_euclidean_algorithm(a, b):
    x1, y1, x2, y2 = 1, 0, 0, 1
    
    while b:
        q = a // b
        a, b = b, a % b
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2

    return a, x1, y1

# 示例
y = 7
n = 69
gcd_result, k, w = extended_euclidean_algorithm(n, y)
if gcd_result == 1:
    print(f'{n} 和 {y} 的最大公约数是 {gcd_result}, 逆元存在，为 {w}')
else:
    print(f'{n} 和 {y} 的最大公约数是 {gcd_result}, 逆元不存在')