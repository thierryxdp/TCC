def freq_palavras(frases):
    dic = {}
    frases=str.split(frases)
    for i in range(len(frases)):
        cont = frases.count(frases[i])
        if i < len(frases):
            dic[frases[i]] = cont
    return dic