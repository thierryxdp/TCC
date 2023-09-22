def freq_palavras(frases):
    frases=str.split(frases)
    i=0
    freq={}
    for palavra in frases:
        if palavra not in freq:
            freq[frases[i]]=list.count(frases,palavra)
        i+=1
    return freq