def freq_palavras(frases):
    d = {}
    frases = list(frases)
    j = []
    for i in frases:
        if i not in j:
        	d[i] = frases.count(i)
       	j.append(i)
    return d