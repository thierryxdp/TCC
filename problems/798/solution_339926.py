def freq_palavras(frases):
    frases=frases.split()
    dicionario = {}
    for c in frases:
        dicionario[c]= frases.count(c)