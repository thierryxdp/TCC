def soma_h(h):
    '''
    função que calcula o valor
    '''
    numero = 0.0
    for caractere in range (1,h+1):
        numero += 1/caractere
    return round (numero,2)