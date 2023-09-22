def colchao(medidas,H,L):
    '''ao receber as medidas do colchão entre colchetes
    e do menor para o maior, a altura H da porta, e a 
    largura L da porta, retorna se colchão passará pela
    porta, ou não.
    list, int, int, -> boolean'''
    if medidas[1] <= H:
        return True
    elif medidas[1] > H and medidas[1] <= L:
        return True
    else:
        return False