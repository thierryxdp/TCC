def posLetra(frase,letra,numero):
    i=0
    ocorre=0
    while i<len(frase):
        if frase[numero+i] in letra:
            ocorre=(numero+i)
        else:
            ocorre=-1
        i=i+1
    return ocorre