# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao que retorne o numero de palavras da frase"""
    frase=str.split(frase)
    return len(frase)