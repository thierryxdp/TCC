def freq_palavras(frases):
    a= str.split(frases)
    dicio={}
    for palavra in a:
        if palavra not in dicio:
            dicio[palavra]=1
            else:
                dicio[palavra]+=1
    return dicio