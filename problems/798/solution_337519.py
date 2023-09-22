def freq_palavras(frase):
    '''Retorna as palavras e a quantidade de vezes que elas aparecem na frase
    	str -> dict'''
    resultado = {}
    palavra = frase[:1]
    for palavra in frase:
     	ocorrencias = str.count(frase, palavra)
        resultado = resultado + {palavra : ocorrencias}
    return resultado