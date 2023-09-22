def posLetra(frase,referente,indice):
    i = 0
    s = []
    while i < len(frase):
        if  frase[i]==referente:
            s = s + [i]
        i = i + 1
    return  s[referente-1]