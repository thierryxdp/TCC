def repetidos(lista):
    '''list -> int'''
    '''retorna quantas vezes um elemento mais se repete na lista'''
    
    i = 0
    a = 0
    
    while i < len(lista):
        
        if list.count(lista,lista[i]) > a:
            a = list.count(lista,lista[i])
            pass
        i += 1
        pass
    return a