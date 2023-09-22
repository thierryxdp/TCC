# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Entre com uma string para retornar o numero de pelavras contida nela
    String -> Int"""

    x = frase.split()

    return int(len(x))