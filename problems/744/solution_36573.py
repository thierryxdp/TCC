# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    l = len(s)
    s1 = l//2
    s2 = s1 + 1
    
    s1 = s[0:s1]
    s2 = s[s2:l]
    return '#'+str.join('#', [s1,s2])+'#'