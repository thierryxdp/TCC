# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''função que insere # no inicio,meio e fim da string'''
    return '#'+ str(s[:(len(s)//2)])+'#'+str(s[(len(s)//2):])+'#'