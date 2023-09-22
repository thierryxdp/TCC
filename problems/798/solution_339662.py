def freq_palavras(frases):
    """ - """
    
    dicionario = {}
    x = frases.split()
    contador = 0

    while contador<len(frase):
        if x[contador] not in dicionario:
            dicionario[x[contador]] = 1
        else:
            dicionario[x[contador]] += 1
        i += 1
    return dicionario