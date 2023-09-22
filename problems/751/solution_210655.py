# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''função que dada uma frase, retorna o numero de palavras
     dessa frase, considerando que a frase pode ter espaços no início
     e no final; str -> int'''
    frase = str.split(frase)
    return len(frase)