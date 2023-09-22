def freq_palavras(frases):
    dic = {}
    i = 0
    frases = str.split(frases,' ')
    while i < len(frases):
        palavra = frases[i]
        quant = list.count(frases,palavra)
        dic[palavra]=quant
        i=i+1
    return dic