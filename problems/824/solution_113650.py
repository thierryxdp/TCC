def uppCons(frase):
    novaFrase = ""
    indiceLetra = 0
    while indiceLetra < len(frase):
        if frase[indiceLetra] in "bcdfghjklmnpqrstvwxyzç":
            novaFrase = novaFrase + str.upper(frase[indiceLetra])
        else:
            novaFrase = novaFrase + frase[indiceLetra]
        indiceLetra = indiceLetra + 1
    return novaFrase