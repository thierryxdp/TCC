# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função conta quantas palavras tem na frase dada"""
    frase = str.split(frase)
    return str.count(frase)