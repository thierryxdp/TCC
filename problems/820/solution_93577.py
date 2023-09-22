def posLetra(frase,letra,numero):
    vezes = 0
    proximo = 0
    while proximo<len(frase):
        if frase in str(letra):
            vezes = vezes + 1
        if vezes==numero:
            return frase.count(str(letra))
        else:
            proximo = proximo + 1