def colchao(medidas,H,L):
    '''Dadas as medidas do colchão, a altura e a largura da porta, retorna True se passa pela porta e Flase se não;
    list[float,float,float],float,float -> bool'''
    porta = [H,L]
    list.sort(porta)
    return medidas[0] <= porta[0] and medidas[1] <= porta[1]