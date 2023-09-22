def posLetra(frase,letra,numero):
    i=0
    ocorre=0
    while i<len(frase):
        if frase[i] in letra:
            ocorre= ocorre + frase[:i]
        i=i+1
    return ocorre