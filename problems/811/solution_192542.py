def colchao(medidas, H, L):
    '''dados as medidas do colchao e, a altura H e a largura L da porta, retorna um True se o colchao passar e False se o colchao nao passar
    list, int, int -> bool'''
    
    if medidas[2] <= H:
        if medidas[1] <= L:
            return True
        else:
            return False
    elif medidas[2] > H:
        if medidas[1] <= H:
            return True
        else:
            return False