def repetidos (lista):
    '''retorne o numero de vezes que um elemento da lista e igual ao anterior'''
    i=0
    numeros=1
    while i<len(lista):
        if lista[i] in '112233445566778899':
            numeros = numeros +1
        i = i+1
    return numeros