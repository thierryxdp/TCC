# Filtra Múltiplos
def filtraMultiplos(lista,n):
    '''Recebe um lista com números, analisa e retorna os múltiplos
    de um número inserido que estiverem dentro desta lista;
    LIST, INT -> LIST'''
    lm =[]
    i = 0
    while i < len(lista):
        if (lista[i])%n == 0:
            lm.append(lista[i])
        i += 1
    return lm