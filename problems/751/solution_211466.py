# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """dada uma frase qualquer é retornado a quantidade de palavras
    str -> int
    """
    frase = str.split(frase)
    return len(frase)