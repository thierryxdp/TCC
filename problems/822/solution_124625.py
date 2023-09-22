def repetidos(numeros):
    '''Função que dada uma lista retorna o número de vezes que um elemento da lista é repetido. 
    list --> int '''
    i = 0
    j = 0
    
    while(i < len(numeros)):
        if numeros[i] == numeros[i-1]:
            j += 1

        if (i == 0):
            j = 0
        i += 1

    return j