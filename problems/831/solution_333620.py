def lingua_p(palavra):
    """ - """

    npalavra = palavra.lower()
    contador = 0
    vogais = ["a","e","i","o","u"]
    contavogais = 0

    while contavogais < len(vogais):
        while contador <len(npalavra):
            if npalavra[contador] == vogais[contavogais]:
                npalavra = npalavra[:contador]+ vogais[contavogais] + "p" + npalavra[contador:]
                contador += 3
            else:
                contador += 1
        contador = 0
        contavogais += 1
    return npalavra