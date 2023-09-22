def qtd_divisores(n):
    qtd=0
    for numero in range(1,n+1):
        if n%numero==0:
            qtd+=1
    return qtd