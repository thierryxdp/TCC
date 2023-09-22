def posLetra(s, l, n):
    i = 0
    lista = []
    while i < len(s):
        if s[i] == l:
            lista += i
        i += 1
    return lista[n - 1]