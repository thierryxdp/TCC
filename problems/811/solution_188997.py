def colchao(medidas,H,L):
    '''Função que dadas as medidas de um colchão e a altura H e largura L de portas, retorna True se o colchao passa pela porta e False se não passa: list,int,int -> bool'''
    [A,B,C] = medidas
    if (B<=H) or (B<=L) or (C<=H) or (C<=L):
        return True
    else:
        return False