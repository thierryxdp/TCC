# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    '''Função que dado a frase(i) como entrada, retorna o numero de palavras da frase, string-->int'''
    i=frase
    t=str.split(i)
    x=len(t)
    return x