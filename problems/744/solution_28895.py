# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    meio= len(s//2)
    primeira= s[0:meio]
    segunda= s[meio:len(s)]
    return '#'+primeira+'#'+segunda+'#'