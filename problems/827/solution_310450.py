def qtd_divisores(x):
    d=0
    e=range(1,x+1)
    for i in e:
        if x%i==0:
            d=d+1
    return d