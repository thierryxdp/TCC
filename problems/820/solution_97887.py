def posLetra(frase, letra , numero):
    b = frase.split()
    a = b.find(letra[:numero])
    return b