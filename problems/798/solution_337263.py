def freq_palavras(frases):
    dici= {}
    frases = frase.split()
    for i in range(len(frases)):
        if i not in dici:
            dici[i] = frases[i]
    return dici