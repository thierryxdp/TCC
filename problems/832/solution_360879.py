def eh_quadrada(matriz):
    """Função que, dada uma matriz, identifica se ela é quadrada ou não; lista->booleano"""
    
    if len(matriz) == 0:
        
        return True
    
    elif len(matriz) == len(matriz[0]):
        
        return True
    
    else:
        
        return False