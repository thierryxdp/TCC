def qtd_divisores(numero):
    qtd = 0
    '''
    for x in range(1, numero + 1):
        if numero % x == 0:
            qtd = qtd + 1 
    '''
    contador = 0
    while contador < len(numero + 1):
        x = qtd[contador]
        qtd = qtd + 1 
        contador = contador + 1

        
    return qtd