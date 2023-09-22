def posLetra(string,letra,n):
    i=0
    indice = []
    while i < len(string):
        if string[i] == letra:
            x = str.find(string,letra,i)
            indice = indice + [x,]
        i = i + 1
    if len(indice) >= n:
        return indice[n-1] 
    else: 
        return -1