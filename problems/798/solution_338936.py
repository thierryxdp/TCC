def freq_palavras(frases):
    wrd = str.split(frases)
    d = {}
    for p in range(len(wrd)):
        frases.count(wrd[p])
        d [wrd[p]] = frases.count(wrd[p])
    return d