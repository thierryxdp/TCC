def qtd_divisores(n):
    lista=[]
    for x in range[2,n]:
        if n%x==0:
            lista.append(x)
    return len(lista)