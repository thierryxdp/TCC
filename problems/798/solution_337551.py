def freq_palavras(frases):
    dicti={}
    newfrases = str.split(frases)
    for caracter in newfrases:
        dicti[caracter]= str.count(caracter,frases)
    return dicti