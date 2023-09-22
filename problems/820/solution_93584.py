def posLetra(frase,letra,numero):
    vezes = 0
    proximo = 0
    while proximo<numero:
        if str(letra) in frase:
            vezes = vezes + 1
        if vezes==numero:
            return frase.count(str(letra))
        else:
            proximo = proximo + 1