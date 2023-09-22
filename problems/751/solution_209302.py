# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Essa função recebe uma frase e retorna a quantidade de palavras nela
    str -> int'''
    f = str.strip(frase)
    quant = str.count(f, ' ') + 1
    return quant