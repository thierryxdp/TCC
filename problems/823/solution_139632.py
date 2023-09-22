def faltante(lista):
    '''list -> int'''
    '''retorna o numero que deveria estar na lista'''
    
    L = lista.sort()
    i = 0
    
    while i < len(lista):
        if L[i] + 1 != L[i+1]:
            return L[i] + 1
        i += 1