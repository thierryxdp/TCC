def posLetra(string,letra,n):
    d=0
    if string.count(letra)<n:
        d=-1
    elif n<=2:
        d=string.index(letra,n)
    elif n>2 and n<4:
        d=string.index(letra,string.index(letra,n)+1)
    elif n>=4:
        d=string.index(letra,string.index(letra,n))+2
      
    return d