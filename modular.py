def mod(a, b):
    remainder = a % b
    if remainder < 0:
        # 调整余数确保非负
        remainder += abs(b)
    return remainder

a = 17
b = 5
remainder = mod(a, b)
print(f'{a} mod {b} = {remainder}')
# 17 mod 5 = 2

a = 25
b = 7
remainder = mod(a, b)
print(f'{a} mod {b} = {remainder}')
# 25 mod 7 = 4

a = 69
b = 23
remainder = mod(a, b)
print(f'{a} mod {b} = {remainder}')