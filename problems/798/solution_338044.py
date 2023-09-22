def freq_palavras(frases):
    i=0
    p={}
    while i<str.split(frases):
        p[str.split(frases)[i]] = str.count(frases, str.split(frases)[i])
        i=i+1
    return p