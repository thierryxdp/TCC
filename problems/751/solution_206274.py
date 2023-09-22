# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    
	'''Função que recebe uma frase e converte a quantidade de palavras em um inteiro'''
	'''str --> int'''
		
    x = str.split(frase)
    return len(x)