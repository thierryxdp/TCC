def qtd_divisores(n):
    divisores=[]
    d=n
    while d!=0:
        if n%d==0:
            list.append(divisores,d)
            d=d-1
        else:
            d=d-1
    return len(divisores)