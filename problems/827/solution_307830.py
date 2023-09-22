def qtd_divisores(x):
    x = len([i for i in range(1,x+1)if not x%i])
    return x