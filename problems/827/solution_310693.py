def qtd_divisores(x):
    y=0
    for e in range (1, x+1):
        if (y%e==0):
            y+=y
    return y