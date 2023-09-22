# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que dada uma frase retorne o número de palavrass da frase,
    str-->2"""
    x = len(str.split(frase))
    return x