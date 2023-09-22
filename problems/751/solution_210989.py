# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Funçao em que dada uma frase retorne o numero de palavras da frase;
    str -> int'''
    frase1=str.strip(frase)
    return (len(str.split(frase1,' ')))