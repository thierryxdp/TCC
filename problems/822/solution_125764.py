def repetidos (lista):
    '''retorne o numero de vezes que um elemento da lista e igual ao anterior'''
    i=0
    numeros=1
    while i<len(lista):
        if lista[i] in '11,22,33,44,55,66,77,88,99,1010,1111,1212,1313,1414,1515,1616,1717,1818,1919,2020,2121,2222,2323,2424,2525,2626,2727,2828':
            numeros = numeros +1
        i = i+1
    return numeros