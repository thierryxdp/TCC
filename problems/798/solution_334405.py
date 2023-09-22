def freq_palavras(frases):
    contagens = []
    elementos = str.split(frases)
    for palavra in elementos:
		qntd = list.count(elementos,palavra)
        contagens.append(qntd)
		for numeros in contagens:
        	dic = {palavra : numeros}
	return dic