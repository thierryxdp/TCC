def freq_palavras(frases):
    dic = {}
    for palavra in frases:
        if palavra in frases:
            dic = dic + {palavra}
    return dic