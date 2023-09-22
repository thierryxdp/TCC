def posLetra(frase,referente,indice):
    i = 0
    s = ''
    while str.count(s,referente) <= indice:
        if str.count(s,referente) <= indice:
            r = len(s)
        i = i + 1
        s += frase[i]
    return  r