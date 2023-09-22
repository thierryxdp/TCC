def posLetra(string,letra,n):
    i=0
    lista = []
    while i < len(string):
        if string[i] == letra:
            lista.append(i)
        i = i + 1
    if lista == [] or n > len(lista):
        r = lista.append(-1)
    else:
        r = lista[n-1]
    return r