# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase = str) -> int:
    """Função que dada uma frase, retorna o número de palavras da frase. Considerando que a frase possa ter espaços no início e no final."""
    x = str.split(str.lstrip(str.rstrip(frase
	return len(x)