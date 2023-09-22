def qtd_divisores(numero):
    proximo=1
    lista=[]
    if numero < 0:
        return 0
    for proximo in range(1,numero+1):
        if numero%proximo==0:
            lista += [proximo]
            proximo += 1
    return len(lista)