# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Dada um frase, retorna o número de palavras dela.
    string -> int'''
    frase_lista=frase.split('')
    return len(frase_lista)