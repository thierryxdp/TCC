def qtd_divisores(numero):
    proximo=1
    lista=[]
    for proximo in range(1,numero+1):
        while numero%proximo==0:
            proximo += 1
            lista += [proximo]
    return lista