def posLetra(frase,letra,numero):

    frase = frase.lower()

    nova_frase = sum(frase.count(i) for i in letra)
    return nova_frase