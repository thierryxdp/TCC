def freq_palavras(frases):
    texto = list(frases)
    dicionario = {}
    for var in texto:
        
        dicionario[var]=str.count(texto,var)
        
    return dicionario