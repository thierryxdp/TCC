# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Função que dada uma frase qualquer, retorna o número de palavras
    contidos na frase, incluindo espaços e pontuações. str -> int'''
    x = str.split(frase)
    return list.count([frase],0,100)