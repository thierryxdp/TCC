def freq_palavras(frase):
    palavras = str.split(frase)
    dicionario={}
    for i in palvras:
        if i in dicionario:
            dicionario[i]+=1
        else:
            dicionario[i]=1
    return dicionario