# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dada uma string s, retorna s com # no início, meio e fim; str -> str'''
    MeioS=(len(s)//2)
    return '#' + s[:MeioS] + '#' + s[MeioS:] + '#'