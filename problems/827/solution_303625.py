def qtd_divisores(n):
    soma=0
    for div in range(1,n+1):
        if n%div==0:
            soma+=1
    return soma