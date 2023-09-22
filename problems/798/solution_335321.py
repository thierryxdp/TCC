def freq_palavras(frases):
    frases=frases.split(' ')
    num=range(0,len(frases))
    for h in num:
        p=frases[h]
        c=frases.count(p)
    return {p:c}