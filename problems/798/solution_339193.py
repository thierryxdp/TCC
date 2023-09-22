def freq_palavras(frases):
    lista = frases.split(' ')
	dic = dict()
    for palavra in lista:
        dic[palavra] = frases.count(palavra)
    return dic