def freq_palavras(frases):
    d = {}
    frases = list(frases)
    j = []
    for i in frases:
        j.append(i)
        if i not in j:
        	d[i] = frases.count(i)
    return d