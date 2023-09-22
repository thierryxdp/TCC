def qtd_divisores(n):
    r=[]
    for x in range(1,n):
        if n % x ==0:
            r = r.append(n)
    return len(r)