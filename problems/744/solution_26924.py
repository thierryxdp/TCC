# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''Dado uma string s, retorne uma string com # no início, meio e fim de s
    string -> string'''
    S=str(s)
    S2=#+S(:len(S)//2)+#+S[len(S)//2:)+#
    return S2