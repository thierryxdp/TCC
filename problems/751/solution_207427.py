# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Calcula a quantidade de palavras de uma frase;
    str -> int"""
    return len(str.split(frase,' '))