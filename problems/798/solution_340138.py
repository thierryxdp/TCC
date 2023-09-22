def freq_palavras(frases):
    d = {}
    frases = frases.replace('.','')
    frases = frases.replace('?','')
    frases = frases.replace('!','')
    frases = frases.replace(',','')
    frases = frases.replace('/','')
    palavras = frases.split()
    for palavra in palavras:
        if palavra not in d:
            d[palavra] = 1
        else:
            d[palavra] += 1
    return d