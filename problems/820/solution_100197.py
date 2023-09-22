def posLetra(frase,letra,indice):
    j=0
    o=0
    if str.count(frase,letra)<indice:
        return -1
    while j<len(frase):
        if frase[j]==letra:
            o=o+1
            return o
    j=j+1