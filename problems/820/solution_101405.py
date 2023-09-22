def posLetra(string,letra,n):
    i=0
    indice = []
    while i < len(string):
        if string[i] == letra:
            x = str.find(string,letra)
            indice = indice + [x,]
        if not letra in string:
            return -1
        i = i + 1
    return indice