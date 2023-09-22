def filtra_pares(elementos):
    '''função que verifica e retorna, a partir de uma tupla com 4 elementos inteiros, uma outra tupla com os elementos pares da anterior; tuple -> tuple'''
    
    resto = elementos[0]%2
    
    if resto==0:
        return elementos[0]