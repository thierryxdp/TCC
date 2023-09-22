def freq_palavras(frase):
    L=list(str.split(frase))
    dicionario={}
    for i in range(0,len(L)):
        x = list.count(L,L[i])
        dicionario[L[i]]=x
    return dicionario