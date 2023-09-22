def posLetra(string,letra,n):
    i=0
    o = 1
    lista = []
    while i < len(string):
        if string[i] == letra:
            lista.append(i)
            o = o + 1
        i = i + 1
    return print(lista[n - 1])