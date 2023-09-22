def qtd_divisores(d):
    a=0
    lista=list(range(1,d+1))
    for num in lista:
        if d%num==0:
            a=a+1
    return a