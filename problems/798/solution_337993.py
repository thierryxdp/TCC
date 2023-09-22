def freq_palavras(frases):
    'str->dict'
    dicio={}
    lista_frase=str.split(frases)
    for palavra in frases:
        dicio={palavra:list.count(frases,palavras)}
    return dicio