def freq_palavras(frases):
    dic={}
    for x in frases:
        if not x in  dic:
            str(x) = frases.count(x)
            return dic