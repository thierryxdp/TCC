# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """a função retorna a quant. de palavras em um frase; str->int"""
	novo_texto = frase.split()#divide a frase em palavras
	return len (novo_texto)