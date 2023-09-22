def freq_palavras(frases):
    dicionario={}
    palavras=str.split(frases)
    for i in palavras:
        dicionario= {palavras[i]:str.count(frases,palavras[i]),}
    return dicionario