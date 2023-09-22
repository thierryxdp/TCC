# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao retorna o numero de palavras na frase"""
    x=frase.split()
    return len(x)