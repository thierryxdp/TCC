def freq_palavras(frases):
    L=list(str.split(frase))
    dicionario={}
    for i in len(L):
        x = list.count(L,L[i])
        list.append(dicionario, L[i]+':'+x)
    return dicionario