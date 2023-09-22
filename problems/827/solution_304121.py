def qtd_divisores(numero):
    '''funcao que retorna quantos divisores o numero dado na entrada possui
    list->int'''
    divisores=0
    for valor in list(range(1,numero+1)):
        if numero%valor==0:
            divisao=numero/valor
            divisores=int((divisao/divisao)+divisores)
    return divisores