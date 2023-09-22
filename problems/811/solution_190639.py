def colchao(medidas,H,L):
    '''Função que retorna se um colchão de lados A,B e C (itens informados em formato de uma lista)consegue passar por uma porta de altura H e largura L'''
    if medidas[0]<=L and medidas[1]<=H:
        return True
    elif medidas[0]<=H and medidas[1]<=L:
        return True
    else:
        return False