def colchao(medidas, H, L):
    '''Função que dada as medidas de um colchão, em uma lista, da menor para a maior, e a altura
    e largura da porta, retorna se o colchão passaria por ela ou não (todas medidas inteiras)
    list, int, int -> bool'''
   	medidas[0] = a
    medidas[1] = b
    medidas[2] = c
    if a * b >= H * L or a * c >= H * L or b * c >= H * L:
        return True
    else:
        return False