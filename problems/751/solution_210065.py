# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''
    Funçao que recebe uma frase e retorna o numero de palavras da frase
    str -> int
    '''
    l=str.split(frase)
    return len(l)