# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    metade= len(s)//2
    parte1= s[0:metade]
    parte2= s[metade:]
    return '#'+parte1+'#'+parte2+'#'