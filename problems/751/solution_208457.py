# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
        dada uma frase, retorna a quantidade de palavras dela.
        str -> int
    '''
    formatada=len(str.split(str.strip(frase,' ')))
    return formatada