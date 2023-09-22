# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Retorna a string s, porém com um # no início, meio e fim.'''
    m = len(s)//2
    novo_s = "#" + s[0:m] + "#" + s[m:] + "#'
    return novo_s