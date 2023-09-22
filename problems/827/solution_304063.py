def qtd_divisores(numero):
    proximo=1
    soma=0
    for proximo in range(1,numero+1,1):
        if numero%proximo==0:
            proximo += 1
            soma += 1
            return soma