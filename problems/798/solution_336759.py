def freq_palavras(frases):
    lista1 = str.split(frases)
    palavras = []
    for p in lista1:
        palavras = palavras + [list.count(lista1,p),]
    dic = dict(palavras)
    return dic