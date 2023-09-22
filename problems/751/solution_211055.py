# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Recebe um texto e retorna a quantidade de palavras separadas por espacos;
    str --> int """

    buffer = len(str.split(frase,' '))

    return buffer