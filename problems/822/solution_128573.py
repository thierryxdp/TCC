def repetidos(lista):
    '''funcao que retorna o numero de vezes que o elemento da lista e igual ao elemento anterior list->int'''
    i = 1
    x = 0
    while i < len(lista):
        
        if lista[i] == lista[i - 1]:
            
            x = x + 1
            
        i = i + 1
        
    return x