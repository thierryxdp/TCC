def posLetra(frase,x,n):
    i=0
    while i<len(frase):
        if x in frase[i]:
            z=str.find(frase,x,n-1,len(frase))
            return z
        if x in frase:
            z=str.find(frase,x,n,len(frase))
        else:
                z=-1
        i=i+1
            
    return z