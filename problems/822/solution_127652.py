def repetidos(lista):
    '''Esta função retorna o numero de vezes que um elemento da lista
    é igual ao elemento anterior.
    list >>> int '''
    i = 0
    a = 0
    
    while i < len(lista)-1:
        if lista[i]! = lista[i+1]:
            if list.count(lista, lista[i])! = 1:
                a += 1
        i += 1
        if lista[i-1] == lista[i] and i == len(lista)-1:
            a += 1
                
    return a