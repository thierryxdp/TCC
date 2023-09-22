def posLetra(frase,referente,indice):
    i = 0
    s = ''
    while str.count(s,referente) <= indice:
        r = len(s)
        n = n + 1
        s += frase[n]
    return  r