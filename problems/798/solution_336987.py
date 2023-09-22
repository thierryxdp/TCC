def freq_palavras(frases:str):
    frases=frases.split()
    dicionario={}
    for palavra in frases:
        dicionario[palavra]=0
    for palavra in frases:
        dicionario[palavra]+=1
    return dicionario