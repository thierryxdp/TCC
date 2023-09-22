def uppCons(frase):
    """Retorna a frase dada com todas as consoantes
    em caixa alta e mantem os outros caracteres como estavam."""
    indiceFrase = 0
    indiceConsoante = 0
    listaConsoantes = []
    consoantes = "bcdfghjklmnpqrstvwxyz"
    while indiceFrase < len(frase) and indiceConsoante < len(consoantes) :
        if consoantes[indiceConsoante] in frase:
            consoanteFrase = frase[frase.index(consoantes[indiceConsoante])]
            frase = frase.replace(consoanteFrase,consoanteFrase.upper())
        indiceFrase += 1
        indiceConsoante += 1
    return frase