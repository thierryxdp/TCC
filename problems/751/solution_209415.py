# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Tem como objetivo receber uma frase e retornar
    o número de palavras dessa frase
    str > int"""
    frase = str.split(frase)
    return len(frase)