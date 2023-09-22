def posLetra(frase,letra,num):
    i=0
    while i<len(frase):
        if letra[i]==len(frase):
            i=i+1
            return i