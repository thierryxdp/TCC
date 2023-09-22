def qtd_divisores(n):
    divisores=[]
    if n<0:
        n=n*(-1)
        d=n
        while d!=0:
        if n%d==0:
            list.append(divisores,d)
            d=d-1
        else:
            d=d-1
    else:
        while d!=0:
        if n%d==0:
            list.append(divisores,d)
            d=d-1
        else:
            d=d-1
    return len(divisores)