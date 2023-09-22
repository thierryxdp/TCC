def freq_palavras(frases):
    L=list(str.split(frase))
    dicionario=[]
    for i in len(L):
        x = list.count(L,L[i])
        if x >1 :
            list.append(dicionario, L[i]:x)
    return dicionario