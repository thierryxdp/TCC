def repetidos(lista):
    '''
    Funçao que recebe uma lista de numeros e retorna o numero
    de vezes que um elemento da lista é igual ao anterior
    list -> int
    '''
    rep = 0
    i=0
    while i<len(lista):
        if lista[i] == lista[i-1]:
            rep = rep + 1
        i = i + 1
    return rep