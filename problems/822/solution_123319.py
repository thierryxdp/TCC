def repetidos(lista):
    '''função que recebe uma lista de numeros e retorna o número de vezes que
    um elemento da lista é igual ao elemento anterior.
    list -> int'''
    i = 0
    listaposicoes = 0
    proximo = i+1
    while i<len(lista):
        if lista[proximo] == lista[i]:
            listaposicoes += 1
        i += 1
        
    return listaposicoes