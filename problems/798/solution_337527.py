def freq_palavras(frase):
    '''Retorna as palavras e a quantidade de vezes que elas aparecem na frase
    	str -> dict'''
	F = frase.split(())
    resultado = {}
	for palavra in F:
        ocorrencia = str.count(F, palavra)
       	resultado[palavra] = ocorrencia
    return resultado