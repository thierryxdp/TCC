# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que pega a frase de entrada e retorna o número de palavras da frase 
    str,str→int"""
	lista=str.split(frase)
    num_palavras=len(lista)
    return num_palavras