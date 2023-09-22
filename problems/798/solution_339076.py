def freq_palavras('frase'):
    dicionario={}
    for palavra in frase:
        if palavra in frase:
            dicionario= dicionario + palavra
    return dicionario