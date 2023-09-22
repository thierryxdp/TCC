def qtd_divisores(n):
    r=[]
    for x in range(1,n):
        if n % x ==0:
            r = list.append(r,n)
    return len(r)