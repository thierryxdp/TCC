def freq_palavras(frases):
dicionario={}
    frases=frases.strip()
    frases=frases.split(' ')
    for palavra in frases:
        if palavra in dicionario:
            dicionario[palavra]=dicionario[palavra]+1
        else:
            dicionario[palavra]=1
    return dicionario