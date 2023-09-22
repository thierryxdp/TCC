def freq_palavras(frases):
    quant=0
    dicionario={}
    a=frases.split()
    for i in range(len(a)):
        quant=list.count(a,a[i])
        dicionario[a[i]]=quant
    return dicionario