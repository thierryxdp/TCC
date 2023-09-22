# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que retorna o número de palavras de uma frase, considerando que esta possa ter espaços no início e no fim
	Entrada: string
	Saída: int"""
	return len(frase.split())