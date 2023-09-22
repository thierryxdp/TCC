# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o número de palavras que a frase contém. str -> int"""
    palavras = frase.split()
	numero_de_palavras = len(palavras)
	return numero_de_palavras