def freq_palavras(frase):
    '''Retorna as palavras e a quantidade de vezes que elas aparecem na frase
    	str -> dict'''
	resultado = {}
    for palavra in frase:
        ocorrencia = str.count(frase, palavra)
        resultado[palavra] = ocorrencia
    return resultado