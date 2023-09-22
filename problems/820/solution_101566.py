def posLetra(string,letra,n):
    d=0
    if string.count(letra)<n:
        d=-1
    elif string.count(letra)>=n:
        d=string.index(letra,string.index(letra,n)+1)
      
    return d