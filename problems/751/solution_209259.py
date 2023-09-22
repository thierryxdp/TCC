# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """função que retorna o numero de palavras de uma frase.
    str->int"""
    listaFrase = str.split(frase, " ")
    return len(listaFrase)