def freq_palavras(frases):
    resultado = dict()
    for frase in frases.split():
        if frase in resultado:
            resultado[frase] += 1
        else:
            resultado[frase] = 1
    return resultado