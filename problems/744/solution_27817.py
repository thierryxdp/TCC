# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna a string s com # no inicio, meio e fim; str -> str'''
    n = len(s)//2
    x=#
    return str(x)+str(s[0:n])+str(x)+str(s[n:])+str(x)