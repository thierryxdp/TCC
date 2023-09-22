def repetidos(numeros):
    '''Função que dada uma lista de números como entrada, retorna o número de
    de vezes que um elemento da lista é igual ao elemento anterior à ele.'''
    list.append(numeros, '')
    indice1 = 0
    indice2 = 1
    contador = 0
    while indice2 + 1 < len(numeros):
        if numeros[indice1] == numeros[indice2]:
            contador = contador + 1
        indice1 = indice1 + 1
        indice2 = indice2 + 1
    return contador