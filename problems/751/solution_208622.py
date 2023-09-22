# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Uma funcao que dada uma frase, 
    retorne o numero de palavras da frase. 
    str->int"""
    frase = str.split(frase)
    return len(frase)