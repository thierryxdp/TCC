def freq_palavras(frases):
    texto = list(frases)
    dicionario = {}
    for var in frases:
        
        dicionario[var]=str.count(texto,var)
        
    return dicionario