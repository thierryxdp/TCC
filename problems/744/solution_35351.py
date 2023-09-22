# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que insere um caractere no inicio,meio e fim
    str->str'''
 return '#' + s[:(len(s)//2)] + '#' + s[(len(s)//2):] + '#'