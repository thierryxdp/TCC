def freq_palavras(frase):
    L=list(str.split(frase))
    dicionario=[]
    for i in L:
        x = list.count(L,L[i])
        list.append(dicionario, L[i]+':'+x)
    return dicionario