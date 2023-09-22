def posLetra(string, letra, n):
    lista=list(string)
    x = 1
    while x < n:
        lista.pop(lista.index(letra))
    return lista.index(letra)