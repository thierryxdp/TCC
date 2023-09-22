# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Retorna a quantidade de palavras em uma frase dada como parâmetro
    	str -> int'''
    return len(str.split(frase, ' '))