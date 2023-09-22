# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
'''retorna a quantidade de palavras em uma frase'''
def quant_palavras(frase):
    frase =  str.split(frase)
    return len(frase)