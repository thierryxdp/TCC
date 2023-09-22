def posLetra(string,letra,n):
    if n<str.find(string,letra,n):
        h=str.index(string,letra,n)
        return h
    elif n==str.find(string,letra):
        return n
    elif n>str.find(string,letra):
        return -1
    elif n<str.find(string,letra):
        return -1