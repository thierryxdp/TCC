def qtd_divisores(x):
    n=0
    for y in range (x+1):
        if x%y==0:
            n=n+1
    return n