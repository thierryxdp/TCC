def qtd_divisores (n):
    soma = 0
    for d in range(1,n+1):
        if n%d == 0:
            soma += d