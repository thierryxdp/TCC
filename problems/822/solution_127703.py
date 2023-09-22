def repetidos(lista):
    '''funcao que retorna o numero de vezes que um elemento da lista aparece nela sendo o wue tem mais repeticoes
    list -> int'''
    proximo = 0
    repetidos = 0
    while proximo<len(lista):
        if lista[proximo]==lista[proximo-1]:
            repetidos=repetidos+1
        proximo= proximo + 1
    return repetidos