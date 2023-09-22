def repetidos(lista):
    '''Retorna o numero de vezes que um elemento da lista é igual ao anterior
    list->int'''
    i=1
    repetidos=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repetidos=repetidos+1
        i=i+1
    return repetidos