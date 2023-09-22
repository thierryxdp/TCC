# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que dado uma frase, retorna o número de palavras da frase
	str -> int"""
    
    numeros = frase.strip()
    numeros = frase.split()
    
    return len(numeros)