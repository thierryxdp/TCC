# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    #Escreve # no comeco no meio e no final da string s
    N=len(s)/2
    R=math.floor(N)
    return '#'+s[0:R]+'#'+s[R:]+'#'