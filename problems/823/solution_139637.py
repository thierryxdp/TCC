def faltante(lista):
    '''list -> int'''
    '''retorna o numero que deveria estar na lista'''
    
    lista.sort()
    i = 0
    
    while i < len(lista) + 1:
        if i + 1 != lista[i]:
            return i
        i += 1