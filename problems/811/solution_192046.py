def colchao(medidas, H,L):
    ''' essa funçao diz se um colchao de medidas A, B e C consegue passar por uma porta de 
    medidas H e L
    lista, int, int ->  bool'''
    if medidas[1] < L and medidas [2] < H:
        return True
    
    else:
        return False