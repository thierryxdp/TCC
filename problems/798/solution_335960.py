def freq_palavras(frases):
    lista = str.split(frases)
    dic = {}
    for palavra in lista:
        repeticoes = list.count(lista,palavra)
        dic[palavra] = repeticoes
	return dic