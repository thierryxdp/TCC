# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que dada uma frase retorne o número de palavras que há nessa frase, os espaços também são considerados. str -> int"""
    return str.count(frase," ") + 1