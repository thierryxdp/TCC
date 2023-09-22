def qtd_divisores(x):
    d=0
    i=1
    while i<(x+1):
        if x%i==0:
            d=d+1
    return d