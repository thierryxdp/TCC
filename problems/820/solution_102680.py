def posLetra(string,letra,n):
    i = 0
    novo = string
    while i < n:
        x= str.index(novo,letra)
        novo= novo[x+1:]
        i += 1
    return len(string) - len(novo)