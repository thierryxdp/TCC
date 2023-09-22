def posLetra(frase,letra,num):
    i = 0
    cont=0
    while i < len(frase):
        if letra in frase:
            cont=cont+1
            i=+1
            return cont
        else:
            return -1