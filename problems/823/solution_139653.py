def faltante(L):
    '''list -> int'''
    '''retorna o inteiro faltante da sequencia'''
    
    L.sort()
    list.append(L,0)
    i = 0
    
    while i <= len(L):
        if i+1 != L[i]:
            return i + 1
        i += 1