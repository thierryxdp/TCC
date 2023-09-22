def repetidos(lista_num):
    '''Dada uma lista de números (lista_num), esta função
    retorna o número de vezes que um elementos da lista
    é igual ao elemento anterior.
    list -> int'''
    
    repeticoes=0
    indice=1
    sucessor=indice-1
    
    while indice<len(lista_num):
        if lista_num[indice]==lista_num[sucessor]:
            repeticoes=repeticoes + 1
        
        indice=indice + 1
        
    return repeticoes