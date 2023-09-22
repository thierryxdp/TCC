def qtd_divisores(n):
    for i in range(1, n//2+1):
        if n % i == 0: 
            yield i
    yield n

n = 47587950
print(list(qtd_divisores(n)))