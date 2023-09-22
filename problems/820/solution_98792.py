def posLetra(string,letra,n):
    if n<str.find(string,letra,n):
        h=str.index(string,letra,n)
        return h
    elif n>=str.find(string,letra):
        return n
    else:
        return -1