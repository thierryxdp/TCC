def qtd_divisores(n):
    lista=[]
    if n<=0:
        return 0
    for x in range(2,n):
        if n%x==0:
            lista.append(x)
    return len(lista)+2