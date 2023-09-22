def faltante(lista):
    '''list -> int'''
    '''retorna o numero que deveria estar na lista'''
    
    L = list.sort(lista)
    i = 0
    
    while i < len(L):
        if L[i] + 1 != L[i+1]:
            return L[i] + 1
        i += 1