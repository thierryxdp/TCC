# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o número de palavras de uma frase
    dada a 'frase' como entrada"""
	frase = str.split(frase)
	return len(frase)