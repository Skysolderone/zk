#最大公约数
def euclidean_alg(a,b):
    while b:
        a,b=b,a%b
    return a
#eg.
num1=20
num2=34
result=euclidean_alg(num1,num2)
print(f'max {result}')
