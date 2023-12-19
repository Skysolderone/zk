#two
def sieve_of_erate(n):
    primes=[True]*(n+1)
    primes[0]=primes[1]=False
    for i in range(2,int(n**0.5)+1):
        if primes[1]:
            for j in range(i*i,n+1,i):
                primes[j]=False
    return [x for x in range(n+1) if primes[x]]


#.eg
limit=20
prime_numbers=sieve_of_erate(limit)
print(f'<={limit},{prime_numbers}')