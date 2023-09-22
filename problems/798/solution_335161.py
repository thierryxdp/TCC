def freq_palavras(frases):
    for h in frases:
        frases=frases.split(' ')
        c=frases.count(h)
    return{h:c}