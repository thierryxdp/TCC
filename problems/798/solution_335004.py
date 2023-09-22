def freq_palavras(frases):
    dicio={}
    frase=frase.split()
    for i in range(len(frase)):
        dicio= dicio + {frase[i]:frase.count(frase[i])}
    return dicio