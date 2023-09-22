def posLetra(frase,letra,n):
    h=[]
    i=0
    if frase.count(letra)<n:
        return -1
    else:
        while frase.count(letra)>n:
            list.remove(frase,letra)
            return i
    i=i+1