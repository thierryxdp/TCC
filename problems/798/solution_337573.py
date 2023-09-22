def freq_palavras(frases):
    ''' '''
    dicionario={}
    for palavra in frases:
        conta_frase= str.count(frases,palavra)
        dicionario={palavra:conta_frase}
    return dicionario