def freq_palavras(frases):
    dic = {}
    i = 0 
    for palavra in frases:
        quant = str.count(frases, palavra)
        dic = dic + {palavra: quant,}
    return dic