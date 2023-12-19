def extended_euclidean_algorithm(a, b):
    x1, y1, x2, y2 = 1, 0, 0, 1
    
    while b:
        q = a // b
        a, b = b, a % b
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2

    return a, x1, y1

# 示例
num1 = 30
num2 = 24
gcd_result, x, y = extended_euclidean_algorithm(num1, num2)
print(f'{num1} 和 {num2} 的最大公约数是 {gcd_result}')
print(f'满足贝祖等式的整数解为：{num1}*{x} + {num2}*{y} = {gcd_result}')
