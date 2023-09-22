# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """define o número de palavras de uma frase qualquer"""
    x = frase.split()
    return len(x)