def quant_palavras(frase):
   '''retorna a quantidade de palavras de uma frase de entrada, considerando que a frase pode ter espaços no início e no final.
   str->int'''
	x= str.split (frase)
	return len(x)