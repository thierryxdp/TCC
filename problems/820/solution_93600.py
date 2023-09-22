def posLetra(frase,letra,numero):
    vezes = 0
    proximo = 0
    while proximo<len(frase):
        if str(letra) in frase:
            vezes = vezes + 1
    		proximo = proximo + 1