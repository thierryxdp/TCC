def colchao(medidas, H, L):
    '''Funcao calcula se é possivel a realizacao de compra de um colchao em promocao para um cliente dadas as medidas da porta e do colchao
lista _ bool'''
    a, b, c = medidas

    if (a<=L and b<=H):
        return True
    else:
        return False