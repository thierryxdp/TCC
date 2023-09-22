def uppCons(frase):
    """Retorna a frase dada com todas as consoantes
    em caixa alta e mantem os outros caracteres como estavam."""
    indice = 0
    listaConsoantes = []
    consoantes = ['a','e','i','o','u']
    while indice < len(frase):
        if consoantes[indice] in frase:
            listaConsoantes.append(frase[indice])
        indice += 1
    return stringConsoantes