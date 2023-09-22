def freq_palavras(frases):
    'str->dict'
    dicio={}
    lista_frases=str.split(frases)
    for frase in lista_frases:
        if frase not in dicio:
            dicio[frase]=list.count(lista_frases,frase)
    return dicio