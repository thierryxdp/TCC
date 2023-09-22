def freq_palavras(frases):
    frases=frases.split(' ')
    i=1
    h=frases[i]
    for h in frases:
        i=i+1
        c=frases.count(h)
    return{h:c}