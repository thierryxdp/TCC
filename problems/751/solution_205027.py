# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """quant_palavras recebe uma frase e devolve a quantidade de palavras que a frase possui.
    str-->int"""
    listaA=str.split(frase)
    return len(listaA)