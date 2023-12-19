def mod_pow(base, exponent, modulus):
    result = 1

    # 将指数展开为二进制形式，从高位到低位逐位处理
    while exponent > 0:
        # 如果当前位是1，则乘上当前的 base，然后取模
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # 将 base 平方，然后取模
        base = (base * base) % modulus
        # 右移一位，相当于除以2
        exponent //= 2

    return result

# 示例：计算 (7^5) % 13
a = 7
c = 5
n = 13
result = mod_pow(a, c, n)
print(f"{a}^{c} mod {n} = {result}")