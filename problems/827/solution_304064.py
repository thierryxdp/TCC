def qtd_divisores(numero):
    proximo=1
    soma=0
    for proximo in range(1,numero+1,1):
        while numero%proximo==0:
            proximo += 1
            soma += 1
            return soma