def freq_palavras(frases):
    'str->dict'
    dicio={}
    lista_frase=str.split(frases)
    for palavra in lista_frase:
        dicio={palavra:list.count(frases,palavra)}
    return dicio