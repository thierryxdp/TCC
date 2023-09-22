# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """retorna o numero de palavras da frase; str -> int"""
    x=str.split(frase)
    return len(x)