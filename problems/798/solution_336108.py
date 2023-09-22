def freq_palavras(frases):
# Funcao que recebe uma string e retorna o dicionario onde cada palavra dessa string e uma chave e tem como valor o numero de vezes em que a palavra aparece
    palavras = frases.split()
    i = 0
    d1 = {}
    for elem in palavras:
        n = list.count(palavras,elem)
		d1[elem] = n
        i +=1
	return d1