def freq_palavras(frases):
    '''Função que recebe uma frase e retorna um dicionário com a quantidade de vezes que as
    palavras aparecem
    str -> dict'''
    palavras = str.split(frases)
    dicionario = {}
    for i in palavras:
        if palavras[i] not in dicionario:
            dicionario[palavras[i]] = 1
		else:
            dicionario[palavras[i]] = dict.get(dicionario, palavras[i]) + 1
	return dicionario