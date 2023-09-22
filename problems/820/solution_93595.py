def posLetra(frase,letra,numero):
    vezes = 0
    proximo = 0
    if str(letra) in frase:
        return str.index(frase.count(str(letra)))