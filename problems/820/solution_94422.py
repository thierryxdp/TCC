def posLetra(frase,letra,número):
    if frase.count(letra)<número:
        return -1
    i=0
    n=0
    while n!=número:
        if letra==frase[i]:
            posição=i-1
            n+=1
        i+=1
    return posição