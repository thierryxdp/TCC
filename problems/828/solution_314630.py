def primo(numero):
    '''função que verifica se um número 
    qualquer é primo.
    int--> bool'''
    
    contador = 0
    
    for elemento in range(2, numero):
        if numero % elemento == 0:
            contador += 1
            
    if contador > 1:
        return False
    else:
        return True