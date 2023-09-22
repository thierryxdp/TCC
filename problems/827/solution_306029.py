def qtd_divisores(n):
    i=1
    lista=[]
    for i in range(n):
        if i<=n:
            if n//i==0:
                lista=lista + i
        i=i+1       
    return lista