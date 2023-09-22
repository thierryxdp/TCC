def freq_palavras(frases):
	lista = frases.split(' ')
    dic = dict()
    for x in lista:
        dic[x] = lista.count(x)
    return dic