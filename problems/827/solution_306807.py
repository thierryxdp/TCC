def qtd_divisores(x):
    for c in range(1,int(x/2+1)):
        if x%c==0:
            return c