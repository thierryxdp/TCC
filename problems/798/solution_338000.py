def freq_palavras(frases):
    'str->dict'
    dici={}
    lista_frase=str.split(frases)
    for palavra in lista_frase:
        dicio={palavra:list.count(lista_frase,palavra)}
        dicio[palavra]=list.count(lista_frase,palavra)
    return dicio