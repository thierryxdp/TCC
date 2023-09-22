# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que recebe uma frase e retorna o numero de palavras da
    frase de entrada"""
    frase = str.split(frase)
    return len(frase)