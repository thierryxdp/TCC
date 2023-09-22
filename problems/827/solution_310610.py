def qtd_divisores(numero):
    '''A função conta os divisores de
    um numero dado como entrada.
    int --> int'''
    
    counter = 0
    
    for elemento in range(1, numero):
        if numero % elemento == 0:
            counter += 1
    if numero <= 0:
        return counter
    else:
        return counter + 1