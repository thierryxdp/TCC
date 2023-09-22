def posLetra(frase,letra,n):
    h=[]
    i=0
    if n<=frase.count(letra):
        while i<len(frase):
            if frase[i]in letra:
                return i
            if n==2:
                if letra in frase[i]:
                    return i
        i=i+1
    if frase.count(letra)<n:
        return -1