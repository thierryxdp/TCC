def posLetra(string,letra,n):
    if str.count(string, letra, n):
        return str.index(string, letra, n)
    else:
        return -1