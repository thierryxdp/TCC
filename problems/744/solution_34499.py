# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    parte1=len(s)//2
    return '#'+s[0:parte1]+'#'+s[parte1:len(s)]+'#'