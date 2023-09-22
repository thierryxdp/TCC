def colchao(medidas, H, L):
    ''' funcao que recebe uma lista e duas unidades de medida e 
        retorna um booleano True ou False, False se o colchao
        nao passa pela porta, e True se ele passa pela porta 
        list, int, int -> bool'''
    if medidas[1] < H:
        return True
    elif medidas[1] > H and medidas[2] > L:
        return False
    elif medidas[1] == H:
        return True
    elif medidas[1] > H and medidas[2] < L:
        return True