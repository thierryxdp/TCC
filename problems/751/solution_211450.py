# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Recebe uma frase e retona o número de palavras contidas nessa 
    frase (str -> int)'''
    palavras = frase.split()
    n_de_palavras = list.count(palavras)
    return n_de_palavras