def posLetra(frase, letra , numero):
    a = letra[:numero]
    b = a.find(a)
    if a in frase:
        return b