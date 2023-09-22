def freq_palavras(frase):
    '''Retorna as palavras e a quantidade de vezes que elas aparecem na frase
    	str -> dict'''
	F = frase.split(( ))
    resultado = {}
	for palavra in F:
        ocorrencia = list.count(F, palavra)
       	resultado[str(palavra)] = ocorrencia
    return resultado