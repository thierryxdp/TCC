# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que conta o número de palavras em uma frase."""
    """string ->int"""
    numero = frase.split()
    return len(numero)