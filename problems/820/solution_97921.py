def posLetra(frase, letra , numero):
    a = letra[:numero]
    b = a.find(frase)
    if a in frase:
        return b
	else a not in frase:
        return b