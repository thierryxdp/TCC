def freq_palavras(frases):
    dic={}
    n=1
    lista=str.slit(frases)
    for p in lista:
        if p in dic:
            dic[p]=dict.get(dic,p)+1
        else:
            dic[p]=1
            return dic