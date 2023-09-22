posLetra(frase,letra,n):
    i=0
    while i<len(frase):
        if letra in frase[i]:
            return i
        i=i+1