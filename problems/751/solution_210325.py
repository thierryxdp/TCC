# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Retorna o numero de palavras de uma frase;
    str => int"""
    lista = str.split(frase)
    return len(lista)