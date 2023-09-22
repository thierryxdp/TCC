def freq_palavras(frases):
    lista = str.split(frases,' ')
    dic = {}
    for p in lista:
        dic[p] = list.count(pista,p)
    return dic