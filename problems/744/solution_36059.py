# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(a):
    b=a[:int(len(a)/2)]
    c=a[int(len(a)/2):]
    return '#'+b+'#'+c+'#'