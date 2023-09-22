def quant_palavras(frase):
	'''funcao retorna a quantidade de palavras em uma dada frase'''
    quantidade = frase.split()
    X = len(quantidade)
    virgula = frase.count(",")

    return X