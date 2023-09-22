def posLetra(frase,referente,indice):
    i = 0
    s = ''
    while str.count(s,referente) <= indice:
        i = i + 1
        s += frase[i]
    return  len(s)