# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """ Função que receba uma string e insire o caractere "#", no ínicio,
    no meio e no fim das entradas
    str -> str """
    x=len(s)
    y= int(x/2)
    z= "#" + str(s)[:y] + "#" + str(s)[y:] + "#" 
    return z