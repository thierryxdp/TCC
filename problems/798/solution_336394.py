def freq_palavras(frases):
    lista = str.strip(frases)
    d = {}
    for i in lista:
        d[i] = list.count(lista,i)