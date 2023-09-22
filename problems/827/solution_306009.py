def qtd_divisores(x):
    y = 0
    for w in range (1, x+1):
        if x/w==0:
            y += 1
    return y