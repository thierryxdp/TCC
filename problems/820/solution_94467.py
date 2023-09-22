def posLetra(string,letra,numero):
    n=numero
    x=0
    y=0
    z=list(string).count(letra)
    while x<len(string):
        if z<n:
            return -1
        elif z>=n:
            a=list(string).index(letra)
            y=a*n
            return y
        elif numero==2:
            return 22