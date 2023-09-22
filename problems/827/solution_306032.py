def qtd_divisores(n):
    i=1
    lista=[]
    for i in range(n):
        if i<=n:
            i=i+1
            if n%i==0:
                lista=lista + [i]
    return lista