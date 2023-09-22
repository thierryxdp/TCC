def faltante(lista):
    '''list -> int'''
    '''retorna o numero que deveria estar na lista'''
    
    i = 0
    
    while i < len(lista):
        if lista[i] + 1 != lista[i+1]:
            return lista[i] + 1
        i += 1