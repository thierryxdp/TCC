def repetidos(lista):
    '''Dada uma lista numérica, retornar o número de vezes que um elemento da lista é igual ao elemento anterior'''
    '''list->int'''
    x=1
    vez=0
    while x<len(lista):
        if lista[x]==lista[x-1]:
            vez=vez+1
        x=x+1
    return vez