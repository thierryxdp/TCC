def primo(numero):
    contador = 0
    '''
    for x in range(1, numero + 1):
    	if numero % x == 0:
     
    '''
    contadorLoop = 0
    lista = range(1, numero + 1)
    while contadorLoop < len(lista):
        x = lista[contadorLoop]
        if numero % x == 0:
            contador = contador + 1
        contadorLoop = contadorLoop + 1
    return contador == 2