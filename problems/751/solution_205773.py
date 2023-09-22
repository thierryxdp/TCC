# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """essa funcao, dada uma frase do tipo str como parametro de entrada,
	 retorna o numero de palavras contidas nela. str -> int"""
    frase_esp = str.strip(frase)
    return len(frase_esp.split())