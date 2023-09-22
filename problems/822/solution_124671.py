def repetidos (numeros):
    '''Dado uma lista de numeros e retorna a quantidade
    de vezes em que um elemento da lista é igual ao
    elemento anterior;
    list-> int'''
    indice=0
    repeticao=0
    n_elementos= len(numeros)
    while indice < n_elementos -1:
        if numeros[indice+1] == numeros [indice]:
            repeticao+=1
        indice+=1
    return repeticao