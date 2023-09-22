def repetidos(lista):
    '''list -> int'''
    '''retorna quantas vezes um elemento é igual ao anterior'''
    
    i = 1
    a = 0
    
    while i < len(lista):
        
        if lista[i] == lista [i-1]:
            a += 1
            pass
        i += 1
        pass
    return a