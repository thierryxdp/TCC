def posLetra(string,letra,n):
    ocorrencias = string.count(letra)
    i = 0
    if ocorrencias<n:
        return -1
    else:
        while i<len(string):
            if string[i] == letra:
                ultima=string[i]
            i=i+1
        return string.find(ultima)