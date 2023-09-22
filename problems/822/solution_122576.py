def repetidos (lista):
    '''função recebe uma lista e retorna o numero de vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    
    i = 0
    rep = 0
    
    while i < len(lista):
        if lista[i] == lista[i-1]:
            rep = rep + 1
        else:
            rep = rep
    
    return rep