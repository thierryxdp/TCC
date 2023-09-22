def freq_palavras(frases):
    dicionario = {}
    lista = str.split(frases)
    for x in lista:
        dicionario[x] = (list.count(lista,x))
    return dicionario