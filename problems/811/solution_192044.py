def colchao(medidas, H,L):
    ''' essa funçao diz se um colchao de medidas A, B e C consegue passar por uma porta de 
    medidas H e L
    lista, int, int ->  bool'''
    if medidas [1] > H or L and medidas [0] > H or L:
        return False
    
    else:
        return True