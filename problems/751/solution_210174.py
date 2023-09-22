# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''função que retorna a quantidade de palavras que há em uma
frase, dada essa mesma frase como entrada.
str -> int'''
    frase_sep=str.split(frase)
    return len(frase_sep)