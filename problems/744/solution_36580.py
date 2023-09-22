# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l = len(s)//2
    s = s[0:l]
    
    return '#'+str.join('#', [s[0:s1], s[:l])+'#'