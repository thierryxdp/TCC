def posstrLetra(frase,letra,numero):
    contar=s.count( letra)
    if frase.index(contar)<numero :
        return frase.index(letra,numero)
    elif frase.index(contar)==0:
        return frase.index(letra,numero)
    elif frase.index(contar)>numero:
        return -1