def freq_palavras(frases):
    dicti={}
    for caracter in frases:
        dicti[caracter]=str.count(caracter,frases)
    return dict.items(dicti)