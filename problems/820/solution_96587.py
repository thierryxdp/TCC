def posLetra(string, letra, n):
    lista=list(string)
    x = 1
    if (letra in string) and (n <= lista.count(letra)):
        while x < n:
            lista.pop(lista.index(letra))
    else:
        return -1
    return lista.index(letra)