def qtd_divisores(n):
    lista=[]
    for c in range(1,n+1):
        if c%n==0:
            lista.insert(c)
        conta=list.count(lista)
    return conta