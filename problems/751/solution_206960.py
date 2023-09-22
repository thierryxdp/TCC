# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao que dada uma frase ela retorna o numero de palavras. considere que pode ter
    espaço no inicio e no final. string->int"""
    return str.count(frase,0,-1)