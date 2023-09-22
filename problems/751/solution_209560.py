# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que retorna a quantidade de palavras de uma frase"""
    fatiando_frase = str.split(frase)
    return len(fatiando_frase)