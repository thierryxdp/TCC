# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Conta quantas palavras a frase possui; str -> int"""
    lista = frase.split(" ")
    tamanho = len(lista)
    return tamanho