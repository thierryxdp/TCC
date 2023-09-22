def repetidos(lista):
    '''retorna quantas vezes um numero repete em relação ao anterior.list->int'''
    i=0
    j=0
    while j<len(lista):
        if lista[i+1]==lista[i]:
            i=i+1
    j=j+1
    return i