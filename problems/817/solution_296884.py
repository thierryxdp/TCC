import math

def acima_da_media(a):
    '''A função retorna uma lista ordenada com as notas
    que ficaram acima da média
    lista->lista'''
    
    
    b = (sum(a)//(len(a)))
    
    i = 0
    u = []
    
    while len(a) > i:
        if a[i] > b:
            list.append(u, a[i])
        i = i + 1
        
    list.sort(u)    
    return u
    
    
    
    return b