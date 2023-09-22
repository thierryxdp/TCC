def posLetra(frase,letra,n):
    h=[]
    i=0
    if frase.count(letra)<n:
        return -1
    while frase.count(letra)==n:
        list.remove(frase,letra)
    return i
        
        if n==1:
            if letra in frase[i]:
                return i
    
        i=i+1