def faltante(lista):
    '''list -> int'''
    '''retorna o numero que deveria estar na lista'''
    
    lista.sort()
    i = 0
    
    while i <= len(lista):
        if i + 1 != lista[i]:
            return i + 1
        i += 1