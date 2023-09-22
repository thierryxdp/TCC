def qtd_divisores(n):
    lista=list(range(1,n+1))
    qtd=0
    for i in lista:
        if n%lista[i]==0:
            qtd=qtd+1
    return qtd