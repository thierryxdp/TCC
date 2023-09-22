# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """A função que conta o número de palavras numa frase.
    str --> int"""
    var=str(frase)
    return str.count(var.strip()," ") + 1