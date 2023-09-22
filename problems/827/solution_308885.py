def qtd_divisores(x):
    d=0
    for i in range(x):
        if x%i==0:
            d=d+1
    return d