def freq_palavras(frases):
    dicionario={}
    for palavra in str.split(frases):
        if palavra in frases:
            dicionario=palavra+1
        return dicionario