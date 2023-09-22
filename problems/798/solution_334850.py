def freq_palavras(frases):
    dic={}
    str.partition(frases,' ')
    for f in frases: 
        dic[f]=1 
        if f==dic: 
            dic[f]+1 
    return dic