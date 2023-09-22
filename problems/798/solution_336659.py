def freq_palavras(frases):
    dic={}
    for i in str.split(frases, ):
        dic[i] = list.count(str.split(frases, ), i)
    return dic