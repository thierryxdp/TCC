def posLetra(frase,letra,x):
    w=list(frase)
    if letra in w[x:]:
        return x+list.index(w[x:],letra)
    else:
        return -1