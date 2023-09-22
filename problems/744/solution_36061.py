# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que receber uma sting e inserir o caractere "#" no inicio , no meio e no fim dela
    str-> str'''
    return "#" + s[0:2] + "#" + s[2:] + "#"