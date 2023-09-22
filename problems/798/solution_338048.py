def freq_palavras(frases):
    i=0
    p={}
    while i < len(str.split(frases)):
        p[str.split(frases)[i]] = str.split(frases).count(str.split(frases)[i])
        i=i+1
    return p