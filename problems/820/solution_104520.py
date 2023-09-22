def posLetra(frase,referente,indice):
    i = 0
    s = []
    while i < len(frase):
        if  frase[i]==referente:
            s = s + [i]
            if (len(s)+1)<indice:
                r = -1
            if (len(s)+1)=>indice:
                r = s[indice-1]
        i = i + 1
    return r