def freq_palavras(frases):
    freq = dict()
    palavras = str.split(frases, ' ')
    
    for palavra in palavras:
        if palavra in freq:
            freq[palavra] += 1
        else:
            freq[palavra] = 1
    return freq