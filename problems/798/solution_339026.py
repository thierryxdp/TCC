def freq_palavras(frases):
    x={}
    stringfrase=str.split(frases)
    for n in stringfrase:
        if not n in x:
            x[n]=list.count(stringfrase,n)
    return x