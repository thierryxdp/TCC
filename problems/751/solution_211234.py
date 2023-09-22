# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''função que recebe uma frase e retorna o número de palavras
    da frase'''
    f = frase.split(' ')
    fr = len(f)
    return fr