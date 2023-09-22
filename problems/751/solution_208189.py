# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dada uma frase, retorna o numero de palavras da frase; str -> int"""
    S = str.split(frase)
    L = len(S)
    return L