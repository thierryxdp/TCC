# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que dada uma frase retorna
    o número de palavras dessa
    """
    frase = str.split(frase)
    return len(frase)