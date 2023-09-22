def freq_palavras(frases):
    dicio={}
    frases=frases.split()
    for i in range(len(frases)):
        dicio= dicio + {frases[i]:frases.count(frases[i])}
    return dicio