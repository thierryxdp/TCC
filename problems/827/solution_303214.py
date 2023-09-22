def qtd_divisores(n):
    lista=[]
    for c in range(1,n+1):
        if c%2==0:
            lista.append(c)
    return len(lista)