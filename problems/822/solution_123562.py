def repetidos(lista):
    '''Recebe como entrada uma lista de números e retorna o 
    número de vezes que um elemento da lista é igual ao elemento anteriorr
    list->int'''
    i=1
    r=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            r=r+1
        i=i+1
    return r