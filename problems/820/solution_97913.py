def posLetra(frase, letra , numero):
    a = letra[0,numero]
    b = a.find(frase)
    if a in frase:
        return b