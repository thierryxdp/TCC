def freq_palavras(frases):
    
    lista_de_palavras = str.split(frases)
    dicionario = {}
    for i in lista_de_palavras:
        if i in dicionario:
            dicionario[i] = dicionario[i] + 1
        if i not in dicionario:
            dicionario[i] = 1
    return dicionario