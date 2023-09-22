def posLetra(frase,referente,indice):
    i = 0
    while str.count(s,referente) <= indice:
        i = i + 1
        s += frase[i]
    return  len(s)