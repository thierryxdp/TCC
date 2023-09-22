def freq_palavras("frase"):
    qnt = {}
	frase = frase.split()
	for i in range(len(frase)):
    	qnt[frase[i]] = 1