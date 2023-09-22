# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Dado uma frase, calcula a quantidade de palavras nela. string > int"""
    frase = str.strip(frase)
    frase = str.split(frase)
    return len(frase)