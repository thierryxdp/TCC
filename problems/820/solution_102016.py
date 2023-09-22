def posLetra(s, l, n):
    i = 0
    lista = []
    while i < len(s):
        if s[i] == l:
            lista += [i]
        i += 1
    if n > len(lista):
        return -1
    else:    
        return lista[n - 1]