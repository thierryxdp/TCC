# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    j=int(len(s)/2)
    sub1=s(0:j)
    sub2=s(j:)
    return '#'+sub1+'#'+sub2+'#'