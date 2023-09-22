def freq_palavras(frases):
    lista = frases.split(' ')
	dic = dict()
    for palavra in lista:
        if len(palavra) > 1:
        	dic[palavra] = frases.count(palavra)
        else:
            dic[palavra] = frases.count(palavra + ' ')
	return dic