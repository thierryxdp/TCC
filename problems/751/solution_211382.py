# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frases):
    '''Func̃ao que dada uma frase, retorna o numero de
palavras da frase
str->str'''
    lista=frases.split(' ')
    qntd=len(lista)
    return qntd