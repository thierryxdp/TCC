# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''funçao que, fornecida uma frase pelo usuario, retorna o numero
    de palavras da frase
    str -> int'''
    frase = str.split(frase)
    return len(frase)