def freq_palavras(frases):
    """
    a partir de um dado texto cria um dicionario com cada 
    palavra do texto e sua quantidade de ocorrencias
    str->dict
    """
    palavras = fraseS.split()
	dict1 = {}
	counter = 0
	for elementos in palavras:
		dict1[palavras[counter]] = palavras.count(palavras[counter])
		counter += 1
	return dict1