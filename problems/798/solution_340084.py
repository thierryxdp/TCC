def freq_palavras(frases):
	palavras=frases.split() 
	dicionario={}
	for i in palavras: 
    	contador=palavras.count(i) 
    	dicionario.update(contador) 
	return dicionario