def freq_palavras(frases):
    dici= {}
    frases = frases.split()
    for i in range(len(frases)):
        if i not in dici:
            dici[frases[i]] = i.count(frases)
    return dici