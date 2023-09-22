def qtd_divisores(n):
    dicio=[range(1,n+1)]
    soma=0
    for i in range(n+1):
        d=n/i
        if d in dicio[:]:
            soma+=1
    return soma