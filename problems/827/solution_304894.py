def qtd_divisores(n):
    soma = 0
    for x in range(1,n+1):
        if n%x==0:
            soma = soma + (n[x],)
    return soma