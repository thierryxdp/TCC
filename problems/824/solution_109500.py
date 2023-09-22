def uppCons(frase):
    """ """
    consoantes="bcdfghjklmnpqrstvwxyzç"
    indice=0
    while indice<len(frase):
        if frase[indice] in consoantes:
            frase[indice].upper()
        indice +=1
    return frase