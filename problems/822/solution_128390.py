def repetidos(lista):
    '''retorna o número de vezes que o elemento da lista é igual ao anterior;
list->int'''
    repetidos=0
    i=1
    

    while i<len(lista):
        if lista[i]==lista[i-1]:
            repetidos= repetidos+1
        i=i+1
    return repetidos