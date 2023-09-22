def freq_palavras(frases):
    dic = {}
    frases = str.split(frases,'')
    for letra in range(len(frases)):
        if frases[letra] in dic:
            dic[frases[letra]] += 1
        else:
            dic[frases[letra]] = 1
    return dic