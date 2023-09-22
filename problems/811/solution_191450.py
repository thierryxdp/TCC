def colchao(medidas,H,L):
    '''Dadas as medidas do colchão, a altura e a largura da porta, retorna True se passa pela porta e Flase se não;
    list[float,float,float],float,float -> bool'''
    return medidas[0] < L and medidas[1] < H