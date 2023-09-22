def posLetra(string,letra,n):
    while n<str.index(string,letra,n):
        return str.index(string,letra,n)
    else return -1