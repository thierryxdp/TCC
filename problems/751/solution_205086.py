# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Dada uma frase, retorna o número de palavras;
str => int'''
    return (str.count(str.rstrip(str.lstrip(frase)),' '))+1