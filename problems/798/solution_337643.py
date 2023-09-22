def freq_palavras(frases):
    dic_freq={}
    i=0
    lista=str.split(frases)
    for lista[i] in lista:
        if lista[i] in lista:
            dic_freq[i]=dic_freq+1
    return dic_freq