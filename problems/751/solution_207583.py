# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase: str):

	lista = frase.split(" ")

	novo_frase = "".join(lista)
	
	return novo_frase