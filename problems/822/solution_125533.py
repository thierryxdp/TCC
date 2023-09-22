def repetidos(lista):
    '''
        Funcao recebe uma lista de numeros e
        retorna o numero de vezes que um elemento
        da lista é igual ao elemento anterior
        list -> int
        
    '''
    i = 1
    repetido = 0
    while i < len(lista):
        if lista[i-1] == lista[i]:
            repetido = repetido + 1
        i = i + 1
    return repetido