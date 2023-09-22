# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """ Faça uma função que retorne o número de palavras da frase
    str -> int
    """
    frase = str.strip(frase, ' ')
    frase_dividida = str.split(frase, ' ')
    quantidade = len(frase_dividida)
    return quantidade