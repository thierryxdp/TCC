def qtd_divisores(numero):
    d=1
    for n in range(numero):
        if numero%d==0:
            d+=d
    return d