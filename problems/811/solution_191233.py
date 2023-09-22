def colchao(medidas,H,L):
    '''Função que a partir das medidas do colchão e da porta calcula
    e informa se o colchão passa pela porta, os dados do colchão
    devem ser informados do menor para o maior
    list, int, int-> bool '''
    if medidas[1]<=H :
        return True
    elif medidas[2]>L:
        return False