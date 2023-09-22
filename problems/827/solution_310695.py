def qtd_divisores(x):
    y=0
    for e in range (1, x+1):
        if (x%e==0):
            y=y+1
    return y