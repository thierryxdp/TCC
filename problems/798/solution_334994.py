def freq_palavras(frases):
    frases=frases.split(' ')
    for h in frases:
        c=frases.count(h)
    return{h:c}