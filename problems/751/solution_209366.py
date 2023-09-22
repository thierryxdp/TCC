# a função retorna o número de palavras da frase.
# string -> int
def quant_palavras(frase):
    a=frase.count(' ')
	a-=2
	return(a)