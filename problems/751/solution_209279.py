# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """
    Essa função recebe uma frase e retorna o número de palavras da frase.
    """
    lista = frase.split(' ')
    return len(lista)