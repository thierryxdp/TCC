def qtd_divisores(n):
    divisores=[]
    d=n
    if n<0:
        return 0
    else:
        while d!=0:
            if n%d==0:
                list.append(divisores,d)
            d=d-1
        return len(divisores)