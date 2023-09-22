def posLetra(string,letra,n):
    n=0
    while n<str.index(string,letra,n):
        if n<str.find(string,letra):
            return str.find(string,letra)
        elif str.find(string,letra)<str.index(string,letra,n):
            return str.index(string,letra,n)
    else:
        return -1