# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que retorna a quantidade de palavras em uma frase
    str --> int"""
    lista1=frase.split()
    return len(lista1)