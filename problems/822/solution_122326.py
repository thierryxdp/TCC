def repetidos(lista):
    '''retorna quantas vezes um numero repete em relação ao anterior.list->int'''
    i=0
    j=0
    j=j+1
    while j<len(lista):
        if lista[i]==lista[i+1]:
            i=i+1
    return i