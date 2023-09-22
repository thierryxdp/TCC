def qtd_divisores (n):
    total = 0
    for i in range (1,n+1):
        if n%i == 0:
            return sum (i)