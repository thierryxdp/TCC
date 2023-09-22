# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''insere uma hashtag # no meio da string inserida'''
    a = int(len(s)/2)
    novo = '#' + s[0:a] + '#'+ s[a:] + '#'
    return novo