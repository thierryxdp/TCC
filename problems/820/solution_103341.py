def posLetra(frase,letra,numero):
    i=0
    ocorre=0
    while i<len(frase):
        if frase[numero] in letra:
            ocorre=(numero+i)
        i=i+1
    return ocorre