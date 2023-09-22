def faltante(L):
    '''função que dada uma lista com (n-1) inteiros de 1 a n, retorna qual número
       não está presente na lista. list -> int'''
    pos = 1
    error_found = 0
    if (L[0] != 1):
        return 1
    while (pos <= len(L) - 1) and (error_found < 1):
        elif (L[pos] != L[pos - 1] + 1):
            error_found = error_found + 1
            numero = L[pos] - 2
        if (L[pos] == L[-1]):
            error_found = error_found + 1
            numero = L[pos] + 1
        pos = pos + 1
    return numero