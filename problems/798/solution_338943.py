def freq_palavras(frases):
    wrd = str.split(frases)
    d = {}
    for p in range(len(wrd)):
        d [wrd[p]] = frases.count(wrd[p])
    return d