# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que retorna o número de palavras da frase dada
    String --> int"""
    s = str.split(frase)
    return len(s)