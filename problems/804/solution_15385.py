def filtra_pares(a):
    '''Retorna somente os elementos pares de uma tupla 
    de 4 elementos em ordem 
    tupla=> tupla'''
    tupla=()
    if par(a[0]) == 0:
        tupla = tupla+(a[0],)
    if par(a[1]) == 0:
        tupla = tupla+(a[1],) 
    if par(a[2]) == 0:
        tupla = tupla+(a[2],)
    if par(a[3]) == 0:
        tupla =tupla+(a[3],)
    return tupla

def par(b):
    '''Retorna se o elemento é par 
    int=> int'''
    if(x%2) == 0:
        return 0
    else:
        return i