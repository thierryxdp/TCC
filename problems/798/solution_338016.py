def freq_palavras(frases):
    i=0
    dic = ''
    while i < len(str.split(frases)):
        dic = dic + str.split(frases)[i] + ':' + str.count(str.split(frases)[i])
    return dic