def medidas (A, B, C):
    ''' Essa funçao calcula a medida de um colchao de largura A, altura B e comprimento C.
    int, int, int -> float'''
    return A*B*C
        
    
def colchao (A,B,C,H,L):
    '''Essa funçao calcula se as medidas do colchao tem tamanho suficiente para passar pela porta, de altura H e largura L.
    lista, int, int -> bool'''
    
medidas = [A, B, C]
           
    if medidas == H*L:
        return True
    elif medidas > H*L:
        return False
    else:
        return True