def posLetra(frase,referente,indice):
    i = 0
    s = ''
    while i < len(frase):
        if str.count(s,referente)==indice:
            s += frase[i]
        i = i + 1
    return  len(s)