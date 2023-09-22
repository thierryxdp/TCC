def freq_palavras(frase):
    separado=str.split(frase)
    dicionario={}
    for palavra in separado:
        if palavra in dicionario:
            dicionario[palavra]+=1
        else:
            dicionario[palavra]=1
    return dicionario