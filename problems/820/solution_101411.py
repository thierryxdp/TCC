def posLetra(string,letra,n):
    i=0
    indice = []
    while i < len(string):
        if string[i] == letra:
            x = str.find(string,letra,i)
            indice = indice + [x,]
        i = i + 1
        return indice[n-1]