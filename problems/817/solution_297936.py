def acima_da_media(lista):
    '''...'''
    
    a = sum(lista)
    b = len(lista)
    c = a/b
    
    if c in list:
        list.remove(c)
        list.append(c)
        list.sort()
        return list[(list.index(c)+1):]