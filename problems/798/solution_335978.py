def freq_palavras(frases):
    dic = {}
    i = 0 
    for palavra in frases:
        quant = str.count(frases, palavra)
        a = [palavra] = quant
        dic = dic + a
       
    return dic