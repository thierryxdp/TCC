def posLetra(string, letra, n):
    lista=list(string)
    x = 1
    if (letra in lista) and (n <= lista.count(letra)):
        while x < n:
            lista.pop(lista.index(letra))
            n = n - 1
    else:
        return -1
    return lista.index(letra) + (n - 1)