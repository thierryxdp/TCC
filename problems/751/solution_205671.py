# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """funcao que dado uma frase retorna a quantidade de palavras nela
    str->int"""
    x=frase.split(' ')
    lista=len(x)
    return lista