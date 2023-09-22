def repetidos(lista):
    '''retorna quantas repetiçoes ocorrem dado uma lista
    list->int'''
    repeticoes=0
    i=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repeticoes+=1
        i+=1
    return repeticoes