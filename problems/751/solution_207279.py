# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Funcao que dada uma frase, retorne o número de palavras da frase.
    string -> int"""
    x = len(str.split(frase))
    return x