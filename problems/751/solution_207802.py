# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Função que retorna a quantidade de palavras na frase
    entrada=string saida=int'''
    x=frase.split(' ')
    return len(x)