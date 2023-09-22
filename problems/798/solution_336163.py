def freq_palavras(frases):
    texto = list(frases)
    dicionario = {}
    for var in texto:   
        dicionario = dicionario[var]=str.count(texto,var)
    return dicionario