def eh_quadrada(matriz):
    '''ve se a matriz é quadrada ou não'''
    contador = 0  
    if len(matriz) == 0:  
        return True  
    
    for elemento in matriz:  
        if len(elemento) == len(matriz): 
            contador += 1  
    if contador == len(matriz):  
        return True  
    else:
        return False