def posLetra(string,letra,n):
    if n<str.find(string,letra):
        h=str.index(string,letra,n)
        return h
    elif n==str.find(string,letra):
        return n
    elif n>str.index(string,letra,n):
        return str.index(string,letra,n)