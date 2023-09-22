def colchao(medidas, H, L):
    '''Função que dada as medidas de um colchão, em uma lista, da menor para a maior, e a altura
    e largura da porta, retorna se o colchão passaria por ela ou não (todas medidas inteiras)
    list, int, int -> bool'''
    if medidas[0] * medidas[1] <= H * L or medidas[0] * medidas[2] <= H * L or medidas[1] * medidas[2] <= H * L:
        return True
    else:
        return False