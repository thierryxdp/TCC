def qtd_divisores(numero):
    divisores=0
    for valor in numero:
        if numero%valor==0:
            x=numero/valor
            divisores=x+divisores
    return divisores