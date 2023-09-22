# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """This function returns the quantity of words in a phrase.
    Give that phrase as the function parameter.
    Str --> int"""
    phrase1 = str.strip(frase)
    words = str.split(phrase1)
    numberOfWDS = len(words)
    return numberOfWDS