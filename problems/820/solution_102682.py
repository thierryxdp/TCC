def posLetra(string,letra,n):
    i = 0
    novo = string
    if n > len(string):
        return -1
    while i < n:
        x= str.index(novo,letra)
        novo= novo[x+1:]
        i += 1
    return len(string) - len(novo)