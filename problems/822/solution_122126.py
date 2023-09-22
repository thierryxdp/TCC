def repetidos(lista):
    '''Recebe uma lista de numeros e retorna o numero de vezes que um elemento
       da lista é igual ao elemento anterior.
       list -> int'''
    i = len(lista)-1
    numeros = []
    while i > 0:
        if [lista[i]] == [lista[i-1]]:
            numeros = numeros + [lista[i]]
        i = i - 1
    return len(numeros)