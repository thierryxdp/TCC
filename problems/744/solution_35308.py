# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''funcao que insere o caractere # no inicio, meio e fim'''
     return '#' + s[:(len(s)//2)] + '#' + s[(len(s)//2)]