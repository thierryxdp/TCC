# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' funcao que recebe caractere # no inicio, meio e final '''
    '''str -> str '''
    x = str('#')
    y = len(s)//2
    return s[0:x] + x + s[:x]