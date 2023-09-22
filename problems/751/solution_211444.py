# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
 	'''Função que recebe uma frase(frase) e retorna o número de palavras
  str -> int'''
	numero_palavras = len(frase.split())
    return numero_palavras