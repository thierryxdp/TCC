def freq_palavras(frases):
    i=0
    p={}
    while i < len(str.split(frases)):
        p[str.split(frases)[i]] = str.count(str.split(frases), str.split(frases)[i])
        i=i+1
    return p