def posLetra(string,letra,n):
    i=0
    lista = []
    quantidade = 0
    while i < len(string):
        if string[i] == letra:
            lista.append(i)
            quantidade = quantidade + 1
        i = i + 1
    if n > quantidade:
        r = - 1
    else:
        r = lista[n-1]
    return r