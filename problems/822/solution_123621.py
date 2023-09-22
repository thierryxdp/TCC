def repetidos(lista):
    '''Função retorna o numero de vezes que um termo se repete
    dada uma lista
    list -> int'''
    i = 1
    lista_nova = list()
    
    while (i<len(lista)):
        if (lista[i] == lista[i-1]):
            list.append(lista_nova, lista[i])
        
        i += 1
    
    return len(lista_nova)