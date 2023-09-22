def freq_palavras(frases):
    "str->dict"
    dicionario=dict()
    for linha in frase:
        linha=linha.strip()
        linha=linha.lower()
        palavras=linha.split(" ")
        
    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] = dicionario[palavra] + 1
        else:
            dicionario[word] = 1
    for qnt in list(dicionario.keys()):
        return(qnt,":"dicionario[qnt])