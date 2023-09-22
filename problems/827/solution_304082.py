def qtd_divisores(numero):
    proximo=1
    lista=[]
    for proximo in range(1,numero+1):
        while numero%proximo==0:
            lista=lista+[proximo]
            proximo=proximo+1
    return lista