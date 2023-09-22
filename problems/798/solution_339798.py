def freq_palavras(frases):
    palavras = str.split(frase)
    ocorrencias = {}
    
	for palavra in palavras:
    	palavra = palavra.lower()
    
    	if palavra in ocorrencia:
       		ocorrencias[palavra] +=1
   			else:
        		ocorrencias[palavra] = 1
        
	return ocorencias