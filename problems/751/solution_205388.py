# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """retorna o número de palavras de uma frase, considerando que a mesma tenha espaços no começo e no final
    str -> int,str"""
    len(frase.split(' '))