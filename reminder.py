def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def chinese_remainder_theorem(congruences):
    """
    中国剩余定理求解函数

    :param congruences: 模线性同余方程组，格式为 [(a1, m1), (a2, m2), ..., (an, mn)]，表示方程组为 x ≡ ai (mod mi)
    :return: 方程组的解 x
    """
    # 计算模数的乘积 M
    M = 1
    for _, mi in congruences:
        M *= mi

    # 计算 Mi 和 Mi 的模逆元素
    M_values = [M // mi for _, mi in congruences]
    Mi_values = [extended_gcd(Mi, mi)[1] for Mi, (_, mi) in zip(M_values, congruences)]

    # 计算解 x
    x = sum(ai * Mi * mi for (ai, _), Mi, mi in zip(congruences, Mi_values, M_values)) % M

    return x

# 示例：解 x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)
congruences = [(2, 3), (3, 5), (2, 7)]
solution = chinese_remainder_theorem(congruences)
print(f"同余方程组的解为 x ≡ {solution} (mod {congruences[0][1] * congruences[1][1] * congruences[2][1]})")