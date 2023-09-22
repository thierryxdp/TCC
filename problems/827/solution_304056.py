def qtd_divisores(numero):
    proximo=1
    for proximo in range(1,numero+1,1):
        if numero%proximo==0:
            proximo += 1
        return proximo