def qtd_divisores(n):
    soma = 0
    for div in range(1,n+1):
        if div%n==0:
            soma = soma + div
    return soma