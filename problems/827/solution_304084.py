def qtd_divisores(numero):
    proximo=1
    lista=[]
    if numero > 0:
        for proximo in range(1,numero+1):
            while numero%proximo==0:
                lista=lista+[proximo]
                proximo=proximo+1
            return lista
    else:
        if numero < 0: 
            for proximo in range(numero,0):
                while numero%proximo==0:
                    lista=lista+[proximo]
                    proximo=proximo+1
                return lista