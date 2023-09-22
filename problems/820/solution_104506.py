def posLetra(frase,referente,indice):
    i = 0
    s = ''
    while str.count(s,referente) <= indice:
        if str.count(s,referente):
            s += frase[i]
        i = i + 1
    return  len(s)