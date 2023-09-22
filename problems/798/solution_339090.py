def freq_palavras(frases): 
    dicionario = {}
    palavra = 0
    for palavra in frases:
        if palavra in '':
            dicionario = dicionario + 1
    return dicionario