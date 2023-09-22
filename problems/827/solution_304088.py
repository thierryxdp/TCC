def qtd_divisores(numero):
    proximo=1
    lista=[]
    if numero > 0:
        for proximo in range(1,numero+1):
            if numero%proximo==0:
                lista=lista+[proximo]
                proximo=proximo+1
            return lista
    else:
        if numero < 0: 
            return 0