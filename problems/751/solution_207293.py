# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dada uma frase, retorna o numero de palavras que contem nela
    string -> int"""
frase = str.split(frase)
	return len(frase)