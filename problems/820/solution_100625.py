def posLetra(frase,letra,n):
    h=[]
    i=0
    if frase.count(letra)==1 and n==2:
        return -1
    while i<len(frase):
        if n==1:
            if letra in frase[i]:
                return i
        if n==2:
            list.remove(frase,letra)
            if letra in frase[i]:
                return i
        i=i+1