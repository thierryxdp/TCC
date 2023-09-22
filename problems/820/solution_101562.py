def posLetra(string,letra,n):
    proximo=0
    d=0
    while proximo< len(string):
        if string.count(letra)<n:
            d=-1
        elif string.count(letra)>=n:
            d=string.index(letra,string.index(n-1))
        proximo=proximo+1
    return d