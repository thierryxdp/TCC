def posLetra(string,letra,n):
    ocorrencias = string.count(letra)
    i = 0
    quantidade = 0
    if ocorrencias<n:
        return -1
    else:
        while quantidade<n:
            if string[i] == letra:
                quantidade = quantidade + 1
            i=i+1
        return i - 1