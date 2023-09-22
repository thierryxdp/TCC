def qtd_divisores(x):
    c=0
    for e in range(1,x+1):
        if x%e==0:
            c=c+1
    return c