def colchao(medidas, H,L):
    ''' essa funçai diz se um colchao de medidas A, B e C consegue passar por uma porta de 
    medidas H e L
    lista, int, int ->  bool'''
    if medidas [1] > H:
        return False
    else: 
        return True
    if medidas [0] > L:
        return False
    else:
        return True