def qtd_divisores(numero):
    proximo=1
    for proximo in range(1,numero):
        if numero%proximo==0:
            proximo += 1
        return proximo