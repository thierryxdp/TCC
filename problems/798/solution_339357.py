def freq_palavras(frases):
    p=frases.split()
    dic={}
    for i in p:
        c=p.count(i)
        dic[i]=c
    return dic