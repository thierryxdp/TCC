def freq_palavras(frases):
    lista1 = str.split(frases)
    palavras = []
    for palavras in lista1:
        palavras = palavras + [list.count(lista1)]
    dic = dict(palavras)
    return dic