def posLetra(string,letra,numero):
    n=numero
    x=0
    y=0
    z=list(string).count(letra)
    while x<len(string):
        if z<n:
            return -1
        elif z>=n:
            list(string).remove(letra)
            return string