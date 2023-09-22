def posLetra(frase,letra,numero):
    i=0
    ocorre=0
    while i<len(frase):
        if letra in frase[:numero]:
            ocorre=ocorre+1
        i+=i+1
    return ocorre