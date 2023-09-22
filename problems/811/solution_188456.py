def colchao(medidas,H,L):
    '''Funçao que, dada as medidas do colchão(ordenadas
    de forma crescente), a altura H e a largura L da
    porta, retorna True se o colchão passsa pela porta
    e False se a dimensões do colchão forem maiores 
    que as dimensões da porta
    list, int, int --> bool'''
    
    if medidas[0]<=L and (medidas[1]<=H or medidas[1]<=L):
        return True 
    else:
        return False