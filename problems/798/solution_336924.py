def freq_palavras(frases):
    dic={}
    for s in frases.split():
        dic[s]=dic.get(s,0)+1
    return dic