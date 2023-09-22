def freq_palavras(frases):
    '''recebe uma string e retorna um dicionário onde cada palavra dessa string é uma chave, que retorna o número de vezes que a palavra apareceu
    str -> dict'''
    conta_palavras = {}
    palavras = frases.split(' ')
    for palavra in palavras:
        if palavra not in conta_palavras:
            conta_palavras[palavra] = 1
        else:
            conta_palavras[palavra] += 1   
	return conta_palavras