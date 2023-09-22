def posLetra(frase,letra,indice):
    j=0
    o=0
    if str.count(frase,letra)<indice:
        return -1
    while j<len(frase):
        if len(o)==indice:
            return j
        elif frase[j]==letra:
            o=o+letra
        
        j=j+1