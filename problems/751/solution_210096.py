'''
A função recebe a frase e cria-se uma variavel
para que separe as palavras da frase, como o
enunciado nos solicita
'''

def quant_palavras(frase):
	
	x = frase.split()
	return x

print quant_palavras("Seja bem vindo")