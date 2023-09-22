# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''retorna string com hashtag inclusa no inicio no meio e fim'''
    '''string ---> string'''
    t = "#" + s[:len(s)//2] + "#" + s[len(s)//2:] + "#"
    return t