def qtd_divisores(n):
    dicio={range(1,n+1)}
    soma=0
    for i in range(1,n+1):
        if n/i==dicio[n/i]:
            soma+=1
    return soma