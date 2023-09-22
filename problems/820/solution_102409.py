def posLetra(string,l,n):
    a=str.count(string,l)
    if a<n:
        return -1
    else:
        return a