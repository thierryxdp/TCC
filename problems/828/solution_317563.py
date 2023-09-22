def primo(numero):
    '''
    
    '''
    
    for num in range(1, numero - 1):
        if numero % num != 0:
            resultado = False
        else:
            resultado = True
    
    return resultado