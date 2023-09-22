# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
	'''funcao que retorna o numero de frases em uma dada string.
	str-->int'''
    x = frase.split()
    return len(x)