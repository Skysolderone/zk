def eul_divistion(a,b):
    quotient,remainder=divmod(a,b)
    if remainder<0:
        #确保余数非负
        remainder+=abs(b)
        #使等式成立
        quotient+=1
    return quotient,remainder
#one
quotient,reminder=eul_divistion(5,6)
print(f'除法实例:商为{quotient},余数为{reminder}')
