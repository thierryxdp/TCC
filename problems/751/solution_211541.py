#A função retorna a quantidade de palavras de uma frase,frase = str
def quant_palavras(frase):
  teste = frase.split(' ')
	return len(teste)

quant_palavras('Joao viado')