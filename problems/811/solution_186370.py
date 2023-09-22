def colchao(medidas, H, L):
    '''Função que dada as medidas de um colchão, em uma lista, da menor para a maior, e a altura
    e largura da porta, retorna se o colchão passaria por ela ou não (todas medidas inteiras)
    list, int, int -> bool'''
   	a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if a * b >= H * L or a * c >= H * L or b * c >= H * L:
        return True
    else:
        return False