def qtd_divisores(n):
    lista=list(range(1,n+1))
    c=0
    for i in lista:
        if n%i == 0:
            c+=1
    return c