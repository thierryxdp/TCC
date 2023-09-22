def posLetra(frase,letra,numero):
    i=0
    ocorre=''
    while i<len(frase):
        if frase[i] in letra:
            ocorre=ocorre+frase[i]
            if ocorre<numero:
                return -1
        i=i+1
    return ocorre