def freq_palavras(frases):
    palavras = str.split(frases)
    dicionario = {}
    for palavras in frases:
        dicionario = {palavra: str.count(palavras,frases)
                     }
    return dicionario