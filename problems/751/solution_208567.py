# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """retorna a quantidade de palavras em uma frase. string-->int"""
    palavras= str.split(frase, " ")
    return len(palavras)