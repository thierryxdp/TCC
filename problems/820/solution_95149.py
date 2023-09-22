def posLetra(string,letra,n):
    """ """
    i=0
    while i<len(string):
        if string.count(letra)>=n:
            return string.count(letra)
        else:
            return -1
        i+=1