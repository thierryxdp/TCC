def colchao(medidas, H, L):
    '''Funcao calcula se é possivel a realizacao de compra de um colchao em promocao para um cliente dadas as medidas da porta e do colchao
lista _ bool'''
    a, b, c = medidas

    if ((a <= L or b <= L) and (b <= H or b<=L or c <= H)):
        return True
    else:
        return False