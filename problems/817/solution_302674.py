def maiores(l,n):
    """list, int -> list"""
    """recebe uma lista e retorna a mesma ordenada e com elementos maiores que n"""
    
    if not n in l:
        list.append(l,n)
        pass
    
    list.sort(l)
    
    N = list.index(l,n) + 1
    
    return l[N:]

def acima_da_media(l):
    """list -> list"""
    """recebe uma lista e retorna os elementos ordenados acima da media"""
    
    m = sum(l)/len(l)
    
    l = maiores(l,m)
    
    return l