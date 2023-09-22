def qtd_divisores(numero):
    proximo=1
    lista=[]
    for proximo in range(1,numero):
        while numero%proximo==0:
            lista += [proximo]
            proximo += 1
    return lista