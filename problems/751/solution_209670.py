# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Esta função conta a quantidade de palavras em uma frase 
	str -> str """

	# retirar espaços
	frase = str.strip(frase,' ')
	# dividir em palavras
	frase_dividida = str.split(frase,' ')
	# contar  quantas existem
	qtd = len(frase_dividida)


	return qtd