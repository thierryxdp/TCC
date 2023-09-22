def repetidos(numeros):
    '''Função que recebe como entrada uma lista de numeros e retorna o 
    numero de vezes que um elemento da lista é igual ao elemento anterior.
    lista -> int'''

    indice = 1
    listadeindices = []

    while indice < len(numeros):
        if numeros[indice] == numeros[indice-1]
        listadeindices += [numeros[indice]]
        indice += 1
    return len(listadeindices)