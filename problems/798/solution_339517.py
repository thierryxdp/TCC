def freq_palavras(frases):
    palavras= frases.split()
    dic = {}
    counter = 0
    for elementos in palavras:
        dic[palavras[counter]] = palavras.count(palavras[counter])
        counter +=1
    return dic