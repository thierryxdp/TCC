def repetidos(lista):
    '''Esta função recebe uma lista e retorna quantas vezes um número dela é igual ao anterior.
list->int'''
    i=0
    x=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            x=x+1
        i=i+1
    return x