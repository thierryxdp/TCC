def freq_palavras(frase):
    '''Retorna as palavras e a quantidade de vezes que elas aparecem na frase
    	str -> dict'''
    for i in range(0,len(frase):
	    resultado = {}
    	palavra = frase[i]
  		for palavra in frase:
     		ocorrencias = str.count(frase, palavra)
        	resultado = resultado + {palavra : ocorrencias}
    return resultado