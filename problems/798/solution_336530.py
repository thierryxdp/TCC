def freq_palavras(frase):
    dicionario={}
    for palavra in frase:
        if palavra in dicionario:
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return dicionario