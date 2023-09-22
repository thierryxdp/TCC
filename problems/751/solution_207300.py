# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Função que conta as palavras de uma frase."""
    """ Str -> Int"""
    frase = frase.strip()
    return len(frase.split(" "))