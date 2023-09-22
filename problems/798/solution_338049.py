def freq_palavras(frases):
    i=0
    dic={}
    while i < len(str.split(frases)):
        dic[str.split(frases)[i]] = str.split(frases).count(str.split(frases)[i])
        i=i+1
    return dic