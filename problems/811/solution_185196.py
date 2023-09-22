def colchao(medidas,H,L):
    '''Funcao que calcula e retorna o valor de altura e largur.
lista,int,int->dupla'''
    A= lista[0]
    B=lista[1]
    
    if (B<=H and A<=L) or (B<=L and A<= H):
    return true
    else:
    return false