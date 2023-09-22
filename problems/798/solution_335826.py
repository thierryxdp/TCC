def freq_palavras(frases):
    dicionario = {}
    pos = frases.index(frases)
    for palavra in frases:
        dicionario = dicionario + palavra:pos
    return dicionario