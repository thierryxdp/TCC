def repetidos(lista):
    '''retorna o numero de vezes que um elemento da lista é igual ao elemento anterior.list->int'''
    i=0
    j=0
    while i<len(lista):
        if lista[i+1]==lista[i]:
            j=j+1
        i=i+1
    return j