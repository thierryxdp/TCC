def freq_palavras(frases):
    palavras = str.split(frases)
    dicionario = {}
    for palavras in frases:
        dicionario = {palavras: str.count(palavras,frases)
                     }
    return dicionario