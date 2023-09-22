def freq_palavras(frases):
    frases = frases.split()
    dicionario = {}
    for palavra in frases:
        qunt_aparece = list.count(frases,palavra)
        dicionario.update({palavra:qunt_aparece})
    return dicionario