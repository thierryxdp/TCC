# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que recebe uma frase e retorna o numero de palavras da frase. str -> int """
    n_palavras = str.split(frase)
    return len(n_palavras)