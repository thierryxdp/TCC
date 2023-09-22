def colchao(medidas,H,L):
    '''Função que, dadas as medidas do colchão (ordenadas 
    de forma crescente), a altura H e a largura L'''
    if medidas[0]<=L and (medidas[1]<=H or medidas[1]<=L):
        return True 
    else:
        return False