def primo(numero):
    '''
    
    '''
    
    for num in range(0, numero - 1):
        if numero % num != 0:
            resultado = False
        else:
            resultado = True
    
    return resultado