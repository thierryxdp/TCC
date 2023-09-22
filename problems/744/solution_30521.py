# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    '''
    insere # no inicio, meio e fim da palavra
    str -> str
    '''
    has=#
    metade=len(palavra)/2
    return str(has)+str(s[0:metade])+str(has)+str(s[metade:])