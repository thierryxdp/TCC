# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Calcula e retorna a quantidade de palavras em uma frase
    str-->int"""
    return frase.count(" ",1,-2)+1