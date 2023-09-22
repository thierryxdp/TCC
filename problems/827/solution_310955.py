def qtd_divisores(n):
    i=0
    for x in range(1,n+1):
        if n%x==0:
            i=i+1
    return i