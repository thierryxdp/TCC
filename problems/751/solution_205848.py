# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que calcula a quantidade de palavras em uma determinada frase
    str -> int """
    y = str.split (frase)
    z = len (y)
    return z