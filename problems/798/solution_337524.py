def freq_palavras(frase):
    '''Retorna as palavras e a quantidade de vezes que elas aparecem na frase
    	str -> dict'''
    for i in range(0, len(frase)):
		resultado = {}
    	palavra = frase[i]
	    for palavra in frase:
    	    ocorrencia = str.count(frase, palavra)
        	resultado[palavra] = ocorrencia
    return resultado