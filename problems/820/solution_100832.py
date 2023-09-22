def posLetra(string,letra,n):
    if n>str.count(string,letra):
        return -1
    else:
        if n==1:
            str.index(string,letra)